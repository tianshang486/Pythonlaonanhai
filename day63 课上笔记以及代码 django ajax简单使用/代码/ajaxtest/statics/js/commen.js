$('#btn').click(function () {
      // ret = requests.post('/login/',date={})  print(ret.content)

      $.ajax({
          url:"{% url 'login' %}",
          type:'post',
          data:{
              uname:$('#username').val(),
              pwd:$('#password').val(),
              {#csrfmiddlewaretoken:$('[name=csrfmiddlewaretoken]').val(),#}
              csrfmiddlewaretoken:"{{ csrf_token }}",
          },
          success:function (res) {

              var resStr = JSON.parse(res);
              console.log(res,typeof res);
              //{"aa":3,"bb":"用户名或者密码错误!!!"}
              if (resStr['aa'] === 3){
                  {#var spanEle = document.createElement('span');#}
                  {#$(spanEle).text(resStr['bb']);#}
                  {#$('form').append(spanEle);#}
                  $('#error').text(resStr['bb']);

              }
              else if(resStr['aa'] === 0){
                  location.href=resStr['bb'];
              }
          }
      })
  })