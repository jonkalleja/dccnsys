!function(t){const a={users:[{id:20,first_name:"Andrey",last_name:"Sidorov",affiliation:"Moscow State University",avatar:"../images/avatar_man.svg"},{id:21,first_name:"Ivan",last_name:"Petrov",affiliation:"Moscow Institute of Physics and Technology",avatar:"../images/avatar_man.svg"},{id:22,first_name:"Kate",last_name:"Petrova",affiliation:"Institute of Control Sciences",avatar:"../images/avatar_woman.svg"},{id:23,first_name:"Maria",last_name:"Ivanova",affiliation:"Tomsk State University",avatar:"../images/avatar_woman.svg"},{id:24,first_name:"Svetlana",last_name:"Sidorova",affiliation:"Ekaterinburg Politechnic Institute",avatar:"../images/avatar_woman.svg"}]};t.fn.authorSearch=function(e){const n=this.find(".dccn-authors-search-content"),i=this.find(".dccn-action-show"),r=this.find(".dccn-action-hide"),s=this.find('input[type="search"]'),o=this.find(".dccn-authors-search-preview"),c=o.find(".dccn-placeholder"),d=o.find(".dccn-content"),l=this.find(".dccn-hidden-form"),u=this.attr("data-source"),f=t.extend({query:()=>{const e=s.val().toLowerCase();return""===u.trim()?new Promise((t,n)=>{setTimeout(()=>{t(a.filter(t=>t.first_name.toLowerCase().includes(e)||t.last_name.toLowerCase().includes(e)||t.affiliation.toLowerCase().includes(e)||String(t.id).includes(e)))},500)}):t.get({url:u,data:t(".dccn-authors-search-form").serialize()})}},e),m=()=>{n.toggleClass("active"),i.toggleClass("d-none")},h=t=>{t.hasClass("active")||(d.toggleClass("active"),c.toggleClass("active"))},v=t=>{Swal.fire({showCancelButton:!0,showCloseButton:!0,buttonsStyling:!1,allowOutsideClick:!1,confirmButtonText:"Add author",customClass:{confirmButton:"btn btn-success btn-lg mr-1",cancelButton:"btn btn-outline-secondary btn-lg"},animation:!1,title:"Confirm add author",html:`\n<div class="dccn-authors-search-modal-item" data-user--id="${t.id}">\n  <img src="${t.avatar}" class="rounded-circle">\n  <div>\n    <h4 class="dccn-text-large-light">\n      ${t.first_name} ${t.last_name}\n    </h4>\n    <p class="dccn-text-0-light text-muted">\n      ${t.affiliation}\n    </p>\n  </div>\n</div>`}).then(a=>{a.value&&(t=>{l.find('input[name="user_pk"]').val(String(t.id)),l.submit()})(t)})},g=()=>{""===s.val().trim().toLowerCase()?h(c):f.query().then(a=>{const e=a.users.map(t=>`\n  <div class="dccn-authors-search-item" \n      data-user--id="${t.id}" \n      data-user--first-name="${t.first_name}" \n      data-user--last-name="${t.last_name}" \n      data-user--avatar="${t.avatar}" \n      data-user--affiliation="${t.affiliation}">\n    <img src="${t.avatar}" class="rounded-circle">\n    <div>\n      <h4 class="dccn-text-2-light">\n        ${t.first_name} ${t.last_name}\n      </h4>\n      <p class="dccn-text-small text-muted">\n        ${t.affiliation}\n      </p>\n    </div>\n  </div>`);e.length>0?(h(d),d.html(e),d.find(".dccn-authors-search-item").click(a=>{const e=a.currentTarget;v({id:t(e).attr("data-user--id"),first_name:t(e).attr("data-user--first-name"),last_name:t(e).attr("data-user--last-name"),affiliation:t(e).attr("data-user--affiliation"),avatar:t(e).attr("data-user--avatar")})})):h(c)})};i.click(m),r.click(m),s.on("input",g),s.on("propertychange",g)},t(".dccn-authors-search").authorSearch()}(jQuery),function(t){t.fn.dccnAvatarUpdateForm=function(){var a=this;a.find('input[type="file"]').change(function(e){var n=this;if(n.files&&n.files[0]){var i=(n.files[0].size/1024).toFixed(4);if(i>1e3)Swal.fire({type:"warning",text:`Profile image size must be under 1000KB, your file is ${i}KB`,customClass:{confirmButton:"btn btn-outline-secondary mx-2"},buttonsStyling:!1});else{var r=new FormData(a.get(0)),s=new FileReader;s.onload=function(e){Swal.fire({text:"Use this as your profile picture?",imageUrl:e.target.result,imageWidth:240,imageHeight:240,imageAlt:"new profile picture",animation:!1,showCancelButton:!0,cancelButtonText:"No",confirmButtonText:"Yes",customClass:{image:"img-fluid rounded-circle",confirmButton:"btn btn-success mx-2",cancelButton:"btn btn-outline-secondary mx-2"},buttonsStyling:!1}).then(i=>{if(i.value){var s=new XMLHttpRequest;s.open("POST",a.attr("data-target"),!0),s.onload=function(t){location.reload()},r.append("avatar",e.target.result),r.append("csrfmiddlewaretoken",t("[name=csrfmiddlewaretoken]").val()),s.send(r),t(a.attr("data-preview")).html('<div style="width: 120px; height: 120px; padding: 30px; margin: 0;"><div class="spinner-border dccn-loading-progress" style="margin: 0; padding: 0; width: 60px; height: 60px;" role="status"><span class="sr-only">Loading...</span></div></div>')}else t(n).val("")})},s.readAsDataURL(n.files[0])}}e.preventDefault()})},t(".dccn-avatar-update-form").dccnAvatarUpdateForm()}(jQuery),function(t){const a=t(".dccn-scores-bar-chart"),e=["rgba(255, 99, 132, 0.2)","rgba(54, 162, 235, 0.2)","rgba(255, 206, 86, 0.2)","rgba(75, 192, 192, 0.2)"],n=["rgba(255, 99, 132, 1)","rgba(54, 162, 235, 1)","rgba(255, 206, 86, 1)","rgba(75, 192, 192, 1)"],i=["Technical Merit","Clarity","Relevance","Originality"];a.each((a,r)=>{const s=t(r).attr("data-scores").split(";").map(t=>t.split(",").map(t=>parseInt(t))),o=s.length,c=i.length;let d=o>0&&o<=3;if(s.forEach(t=>{d=d&&t.length===c,t.forEach(t=>{d=d&&!isNaN(t)})}),d){const t=s.length>1?math.add(...s):s[0],a=math.divide(t,o),c=[];s.forEach((t,a)=>{c.push({label:`Review #${a+1}`,data:t,backgroundColor:e[a],borderColor:n[a],borderWidth:1})}),c.push({label:"Average",data:a,backgroundColor:e[o],borderColor:n[o],type:"line",fill:!1}),new Chart(r,{type:"bar",data:{labels:i,datasets:c},options:{scales:{yAxes:[{ticks:{beginAtZero:!0}}]}}})}})}(jQuery),jQuery('[data-toggle="tooltip"]').tooltip(),function(t){t(".dccn-custom-file input.custom-file-input").change(function(){var a=t(this)[0].files[0].name;t(this).next(".custom-file-label").text(a)})}(jQuery),$(document).ready(function(){$(".current-year").text((new Date).getFullYear())}),$(document).ready(function(){const t=$("body");t.on("click",".inst-form-btn[data-form-id][data-value][data-name]",t=>{const a=$(t.target),e=$(a.attr("data-form-id")),n=a.attr("data-value"),i=a.attr("data-name");e.find(`input[name=${i}]`).val(n),e.submit()});const a=function(t){const a=t.serialize(),e=t.parents("[data-html-src]");$.ajax({url:t.attr("action"),method:t.attr("method"),data:a}).done(function(){if(t.hasClass("inst-form-delete"))e.remove();else if(e.length>0){const t=e.attr("data-html-src");$.get(t,function(t){e.html(t)})}else window.location.reload(!0)}),e.html('<div class="d-flex"><div class="mx-auto text-center"><div class="spinner-border"></div><p>Loading</p></div></div>')};t.on("submit","form.inst-form",t=>{const e=$(t.target),n=e.parents(".modal");return n.length>0?(n.on("hidden.bs.modal",function(){a(e)}),n.modal("hide")):a(e),t.stopPropagation(),!1})}),function(t){t.fn.dccnFileInput=function(){var t=this.find(".dccn-file-name");return this.find('input[type="file"]').on("change",function(){this.files&&this.files[0]&&t.text(this.files[0].name)}),this},t.fn.dccnFormSubmitIndicator=function(){return t(this.attr("data-form")).submit(t=>{var a=this.find(".dccn-submit-indicator");this.prop("disabled",!0),a.removeClass("d-none")}),this},t.fn.dccnFileVD=function(){var t=this.find(".dccn-file-vd-form"),a=this.find(".dccn-file-vd-box");return t.on("submit",e=>{var n=new XMLHttpRequest;return n.onload=(()=>{a.html(n.response)}),n.open(t.attr("method"),t.attr("action"),!0),n.send(new FormData(t.get(0))),e.preventDefault(),!1}),this},t(".dccn-file").dccnFileInput(),t(".dccn-submit").dccnFormSubmitIndicator(),t(".dccn-file-vd").dccnFileVD()}(jQuery),function(t){t.fn.reorder=function(){const a=this.find(".dccn-reorder-list"),e=this.find(".dccn-reorder-form"),n=this.find(".dccn-reorder-form-input"),i={value:void 0};n.change(function(){e.submit()});const r=()=>{const a=this.find(".dccn-reorder-list-item"),e=t.map(a,a=>t(a).attr("data-id"));n.val(String(e)),void 0===i.value?i.value=n.val():i.value!==n.val()&&n.trigger("change")};a.sortable({revert:!0,stop:r,create:r})},t(".dccn-reorder").reorder()}(jQuery);