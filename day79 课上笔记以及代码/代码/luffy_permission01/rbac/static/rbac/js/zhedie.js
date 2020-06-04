$('.multi-menu .title').click(function(){
  $(this).siblings('.body').toggleClass('hidden').parent().siblings().find('.body').addClass('hidden')
})