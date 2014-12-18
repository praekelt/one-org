var basic_ajax={XMLHttpFactories:[function(){return new XMLHttpRequest()},function(){return new ActiveXObject("Msxml2.XMLHTTP")},function(){return new ActiveXObject("Msxml3.XMLHTTP")},function(){return new ActiveXObject("Microsoft.XMLHTTP")}],sendRequest:function(url,callback,errback,postData){var req=basic_ajax.createXMLHTTPObject();if(!req)return;var method=(postData)?"POST":"GET";req.open(method,url,true);if(postData)
req.setRequestHeader('Content-type','application/x-www-form-urlencoded');req.onreadystatechange=function(){if(req.readyState!=4)return;if(req.status!=200&&req.status!=304){if(errback)errback(req);return;}
callback(req);}
if(req.readyState==4)return;req.send(postData);},createXMLHTTPObject:function(){var xmlhttp=false;for(var i=0;i<basic_ajax.XMLHttpFactories.length;i++){try{xmlhttp=basic_ajax.XMLHttpFactories[i]();}
catch(e){continue;}
break;}
return xmlhttp;},};window.onload=function(){var last_activity_time=(new Date).getTime();document.onmousemove=function(event){last_activity_time=(new Date).getTime();};function load_new_comments(){if((new Date).getTime()-last_activity_time<30000){var els=document.getElementsByTagName('div');for(var i=els.length-1;i>-1;i--){var el=els[i];if(el.className.indexOf('comment-list-placeholder')>-1){var url='/fetch-new-comments-ajax/'+el.getAttribute('content_type_id')+'/'+el.getAttribute('oid')+'/'+el.getAttribute('last_comment_id')+'/';basic_ajax.sendRequest(url,function(xml_obj){if(xml_obj.responseText)
el.outerHTML=xml_obj.responseText;});break;}}}
window.setTimeout(load_new_comments,15000);}
window.setTimeout(load_new_comments,15000);};if(typeof $!='undefined')
{$(document).ready(function(){if($.support.ajax)
{$(document).on('click','div.foundry-listing div.pagination a, div.foundry-listing div.jmbo-view-modifier div.item a',function(e){e.preventDefault();var url_provider=$(this).parents('div.foundry-page-tile:first');if(url_provider.length)
{var url=url_provider.attr('original_url');var target=$('div.foundry-listing:first',url_provider);}
else
{target=$(this).parents('div.foundry-listing:first');url=$(location).attr('href');}
var listing_dom_id=target.attr('id');if(listing_dom_id=="foundry-listing-")
listing_dom_id=null;url=url.split('?')[0];url=url+$(this).attr('href');$.get(url,{},function(data){var el=$('<div>'+data+'</div>');if(listing_dom_id)
var content=$('#'+listing_dom_id,el);else
var content=$('div#content div.foundry-listing:first',el);target.html(content.html());$(document).trigger("onListingRefresh",[target]);});});$(document).on('click','div.foundry-comments-list div.pagination a',function(e){e.preventDefault();target=$(this).parents('div.foundry-comments-list:first');url=$(location).attr('href');url=url.split('?')[0];url=url+$(this).attr('href');$.get(url,{},function(data){var el=$('<div>'+data+'</div>');var content=$('div#content div.foundry-comments-list:first',el);target.html(content.html());$(document).trigger("onCommentsPaginate",[target]);});});var _submit_intercept_common=function(sender,event,target){event.preventDefault();var url=$(sender).attr('action');if((!url)||(url=='.'))
url=target.attr('original_url');var data=$(sender).serialize();$.ajax({url:url,data:data,async:false,type:'POST',cache:false,success:function(data){if(data.indexOf('{')==0)
{var obj=$.parseJSON(data);$(obj.render_target).html(obj.html);}
else
if(data.search('id="content"')!=-1)
{var el=$('<div>'+data+'</div>');var content=$('div#content',el);target.html(content.html());}
else
target.html(data);}})};$(document).on('submit','div.foundry-enable-ajax .foundry-container form',function(event){event.stopImmediatePropagation();var target=$(this).parents('div.item:first');_submit_intercept_common(this,event,target);});$(document).on('submit','div.foundry-enable-ajax form',function(event){var target=$(this).parents('div.foundry-enable-ajax:first');_submit_intercept_common(this,event,target);});$(document).on('submit','form.comment-form',function(event){event.preventDefault();var form=$(this);var url=$(this).attr('action');var data=$(this).serialize()+'&paginate_offset=-1';;$.ajax({url:url,data:data,async:false,type:'POST',cache:false,success:function(data){if(data.indexOf('{')==0)
{var obj=$.parseJSON(data);$('div.comment-list').html(obj.html);var el=$('#id_comment');el.val('');$('#c'+obj.obj_id).attr('tabindex',-1).focus();}
else
form.replaceWith(data);},complete:function(){$('#id_in_reply_to').val('');}})});$(document).on('click','div.foundry-comments-list a.report',function(){if(!window.confirm('Are you sure you want to report this?'))
return false;var el=$(this);var url=el.attr('href');$.ajax({url:url,async:true,type:'GET',cache:false,success:function(data){el.replaceWith('Reported');}});return false;});}});}
if(typeof $!='undefined')
{$(document).ready(function(){$('div.videoembed-detail, div.foundry-listing div.item-videoembed').each(function(){var el=$(this);var iframe=$('iframe',el);var wo=iframe.width();var ho=iframe.height();var w=el.width();var h=(ho*w*1.0)/wo;iframe.attr('width',w);iframe.attr('height',h);});});}
if(typeof $!='undefined')
{$(document).ready(function(){$(document).bind('onListingRefresh',function(event,target){$('div.gpt-ad',target).each(function(){var el=$(this);var id=el.attr('id');var slot_name=el.attr('slot_name');var width=parseInt(el.attr('width'));var height=parseInt(el.attr('height'));var targeting_key=el.attr('targeting_key');var targeting_values=el.attr('targeting_values').split('|');googletag.defineSlot(slot_name,[width,height],id).addService(googletag.pubads()).setTargeting(targeting_key,targeting_values);googletag.enableServices();googletag.display(id);});});});}