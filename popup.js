window.addEventListener('load', function () {

  getURL()

  chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
    console.log(url);
    // use `url` here inside the callback because it's asynchronous!
  });

  console.log("HEY")
  makeBoxes(24);

  let switchports = document.querySelectorAll(".square");

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
        // xhttp.open('POST', 'http://localhost:8008/')
        // xhttp.send()
        // xhttp.onload = function(){
        console.log("HEY")
        // }
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


function makeBoxes(Howmany)
{
  var square = ""
  var id = 0
  for(var i = 0; i < Howmany; i++)
    {
      console.log("Port " + i)
      // document.getElementById("switch-ports").insertAdjacentHTML("afterend", square)
      id = i + 1
      square = "<div id='" + id + "' class='square'></div>"
      document.getElementById("switch-ports").innerHTML += square;
    }
}

function getURL()
{
  alert("The URL of this page is: " + window.location.href);
}