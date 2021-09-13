window.addEventListener('load', function () {

  chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
    console.log(url);
    // use `url` here inside the callback because it's asynchronous!
  });

  let switchports = document.querySelectorAll(".square");

  let CORS_baseURL = "https://cors-anywhere.herokuapp.com/"

  console.log(switchports)
  var xhttp = new XMLHttpRequest();

  var port = 0;
  
 
  function setCurrentPort(portnumber){
    port = portnumber;


  }

  function getCurrentPort(){
    return port;
  }

  updatePlaceholderInfo();

  for (i = 0; i < switchports.length ; i++) {
      console.log(switchports[i])
      switchports[i].addEventListener('click', function(event) {
        // alert('hey');
        makeOthersStayTheSame();
        button = event.target;
        setCurrentPort(button.id)
        button.classList.add("blueSquare");
        updatePlaceholderInfo();
        xhttp.open('POST', 'http://localhost:8008/')
        xhttp.onload = function(){

          console.log("HEY")
        }
        xhttp.send()

      })

    }


  function makeOthersStayTheSame(){
    for (i = 0; i < switchports.length ; i++) {
      switchports[i].classList.remove("blueSquare");
    }
  }

  function updatePlaceholderInfo(){
    let portinfoRef = document.querySelector("#port-info");
    console.log("THIS IS: "+portinfoRef.innerHTML)
    portinfoRef.innerHTML = ("This is port no. "+ getCurrentPort() )

  }
});
