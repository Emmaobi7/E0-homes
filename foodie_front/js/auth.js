const host5 = 'http://localhost:5000';

// Get the modal
let modalsignup = document.getElementById("sign-up");
let modallogin = document.getElementById("login")

// Get the button that opens the modal
let btnsignup = document.getElementById("myBtnsignup");
let btnlogin = document.getElementById("myBtnlogin");

// Get the <span> element that closes the modal
let closesignup = document.getElementsByClassName("closeSignup")[0];
let closelogin = document.getElementsByClassName("closeLogin")[0];


btnsignup.onclick = function() {
  modalsignup.style.display = "block";
}

btnlogin.onclick = function() {
    modallogin.style.display = "block";
}


closesignup.onclick = function() {
    modalsignup.style.display = "none";
}

closelogin.onclick = function() {
    modallogin.style.display = "none";
}


window.onclick = function(event) {
  if (event.target == modalsignup) {
    modalsignup.style.display = "none";
  }
  if (event.target == modallogin) {
    modallogin.style.display = "none";
  }
}


//auth logic

const signUpForm = document.getElementById('signUp-form');
const loginForm = document.getElementById('login-form');
   
  
let handleLoginForm = async function onLogin (e) {
  e.preventDefault();
  const loginData = new FormData(e.target)
  const data = {
    email: loginData.get('email'),
    password: loginData.get('password')
  }

 
  try {
    const options = {headers: { 'Content-Type': 'application/json'  }};
    const response = await axios.post(`${host5}/auth/login`, data, options)

    localStorage.setItem('userId', response.data.data)
    loginForm.reset();
    window.location.replace("./index.html");
  } catch(err) {
    if (err.response.status === 401) {
      document.querySelector('.loginerror').innerHTML = 'Invalid Email or Password!'
      console.log('Invalid credentials')
    }
    
  }
}

let handleSignUpForm = async function onSignUp (e) {
  e.preventDefault()
  const signUpData = new FormData(e.target)
  const data = {
    email: signUpData.get('email'),
    first_name: signUpData.get('first_name'),
    password1: signUpData.get('password1'),
    password2: signUpData.get('password2'),
  }
  try {
    const options = {headers: { 'Content-Type': 'application/json'  }};
    const response = await axios.post(`${host5}/auth/sign_up`, data, options)
    localStorage.setItem('userId', response.data.data)
    signUpForm.reset();
    window.location.replace("./index.html");
  } catch(err) {
    if (err.response.data.error === "Passwords don't match") {
      document.querySelector('.error').innerHTML = 'Passwords do not match!'
      console.log('please check your passwords')
    }
    if (err.response.data.error === "Email already exists") {
      document.querySelector('.error').innerHTML = 'Email already in use!'
      console.log('We already have this email')
    } 
  }
}

signUpForm.addEventListener('submit', handleSignUpForm)
loginForm.addEventListener('submit', handleLoginForm)

async function logout() {
  try {
    const response = await axios.post(`${host5}auth/logout`)
    localStorage.removeItem('userId')
    window.location.replace("./auth.html");
  } catch(err) {
    console.log(err)
  }
}


