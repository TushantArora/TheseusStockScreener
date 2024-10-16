<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login</title>
  <style>
    *{
      margin: 0;
      padding:0;
      box-sizing: border-box;
      font-family: "Poppins", sans-serif;
    }

    body{
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      background: url(Stock_BG.png) no-repeat;
      background-size:cover;
      background-position: center;
    }
    .wrapper{
      width: 420px;
      background: transparent;
      border: 2px solid rgba(0,0,0,.2);
      backdrop-filter: blur(30px);
      box-shadow: 0 0 10px rgba(0,0,0,.2);
      color: white;
      border-radius: 20px;
      padding:30px 40px;
    }
    .wrapper h1{
      font-size: 36px;
      text-align: center;
      padding-bottom: 20px;
    }
    .wrapper .input-box{
      width:100%;
      height: 50px;
      /* background: salmon; */
      margin: 30px 0;
    }
    .input-box input {
      width: 100%;
      height: 100%;
      background:transparent;
      border:none;
      outline: none;
      border: 2px solid rgba(255,255,255,.2);
      border-radius: 40px;
      font-size: 18px;
      color: white;
      padding: 20px 45px 20px 20px;
    }
    .input-box input::placeholder{
      color:white;
    }
    .wrapper .remember-forgot{
      display: flex;
      justify-content: space-between;
      font-size: 14.5px;
      margin: -15px 0 15px;
    }
    .remember-forgot label{
     accent-color: white;
     margin-right: 3px; 
    }
    a{
      color:white;
      text-decoration: none;
    }
    a:hover{
      text-decoration: underline;
    }
    .wrapper .btn{
      width: 100%;
      height: 45px;
      background: white;
      border:none;
      outline: none;
      border-radius: 40px;
      box-shadow: 0 0 10px rgba(0,0,0,.1);
      cursor: pointer;
      font-size: 16px;
      color: #333;
      font-weight: 600;
    }
    .btn:hover{
      color:white;
      background: #333;
    }
    .register-link{
      font-size: 14.5px;
      text-align: center;
      margin: 20px 0 15px;
      font-weight: 1200px;
    }
    .error{
      display: flex;
      justify-content: center;
      padding: 10px;
      border: 2px solid red;
      border-radius: 10px;
      
    }
    
  </style>
</head>
<body>
  <div class="wrapper">
    <form id="form_login">
      <h1>Login</h1>
        <div class="input-box">
        <input type="text" name="uname" placeholder="Username" >
      </div>
      <div class="input-box">
        <input type="password" name="password" placeholder="Password" >
      </div>
      <div class="remember-forgot">
        <label><input type="checkbox">Remember me</label>
        <a href="#">Forgot Password?</a>
      </div>
      <button type="submit" class="btn">Start Trading</button>
      <div class="register-link">
        <p>Don't have an account?<a href="#">Register</a></p>
      </div>
    </form>
  </div>
  <script src="https://code.jquery.com/jquery-3.7.1.js" integrity="sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4=" crossorigin="anonymous"></script>
  <script>
    $("#form_login").submit(function(e){
      e.preventDefault();
      var form_data=$(this).serialize();
      $.ajax({
        url:'Login.php',type:'post', dataType:'json', data:form_data,
        success:function(result){
          if(result.msg=='ok'){
            window.open("main.php","_self");
          } else{
            alert("Wrong User ID/Password")
          }
        }
      })
    })
  </script>
</body>
</html>