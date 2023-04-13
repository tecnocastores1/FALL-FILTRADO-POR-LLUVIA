// Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
  apiKey: "AIzaSyB1Z4ylKD4ZjSozWh_g5vP2glTe-Fb2HH4",
  authDomain: "fall-5ad86.firebaseapp.com",
  databaseURL: "https://fall-5ad86-default-rtdb.firebaseio.com",
  projectId: "fall-5ad86",
  storageBucket: "fall-5ad86.appspot.com",
  messagingSenderId: "288860065876",
  appId: "1:288860065876:web:47802559118c4799921dc1"
};
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  const auth =  firebase.auth();

  //signup function
  function signUp(){
    var email = document.getElementById("email");
    var password = document.getElementById("password");

    const promise = auth.createUserWithEmailAndPassword(email.value,password.value);
    //
    promise.catch(e=>alert(e.message));
    alert("Cuenta con exito ");
 
 

  }

  //signIN function
  function  signIn(){
    var email = document.getElementById("email");
    var password  = document.getElementById("password");
    const promise = auth.signInWithEmailAndPassword(email.value,password.value);
   window.location.href = "principal.html";

    
  }


  //signOut

  function signOut(){
    auth.signOut();
    alert("SignOut Successfully from System");
  }

  //active user to homepage
  firebase.auth().onAuthStateChanged((user)=>{
    if(user){
      var email = user.email;
      alert("Usuario Activo "+email);

    }else{
      alert("Usuario Activo")
    }
  })