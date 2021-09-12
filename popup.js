window.addEventListener('load', function () {

  // getURL()
  // FetchDNAC()

  chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
    let url = tabs[0].url;
    console.log(url);
    // use `url` here inside the callback because it's asynchronous!
  });

  // console.log("HEY")
  makeBoxes(24);

  // fetchDNAC();

  let switchports = document.querySelectorAll(".square");
  let save_button = document.querySelectorAll(".fakeButton");

  // console.log(switchports)
  var xhttp = new XMLHttpRequest();

  var port = 0;



  function setCurrentPort(portnumber) {
    port = portnumber;
  }

  function getCurrentPort() {
    return port;
  }

  updatePlaceholderInfo();

  for (i = 0; i < switchports.length; i++) {
    // console.log(switchports[i])
    switchports[i].addEventListener('click', async function (event) {

      button = event.target;
      // alert()
      if (button.id === '0') {
        // They clicked on save 
        alert('Button Clcked');
      }
      else {
        makeOthersStayTheSame();
        // button = event.target;
        setCurrentPort(button.id)
        button.classList.add("blueSquare");
        updatePlaceholderInfo();

        var body = {
            "ip" : "10.0.0.20",
            "interface" : {
              "name" : "GigabitEthernet",
              "id" : "1/0/5",
              "status" : "shut"
            }
        }
        let b = await httpCall('POST','http://localhost:8008/', JSON.stringify(body))
      }
    })

    function saveConfigButton()
    {
      alert('Button Clcked');
    }

  async function getCurrentTabURL() {
  let queryOptions = { active: true, currentWindow: true };
  let [tab] = await chrome.tabs.query(queryOptions);
  url = await tab.url
  return url;
}


  function makeOthersStayTheSame() {
    for (i = 0; i < switchports.length; i++) {
      switchports[i].classList.remove("blueSquare");
    }
  }

  function updatePlaceholderInfo() {
    let portinfoRef = document.querySelector("#port-info");
    // console.log("THIS IS: " + portinfoRef.innerHTML)
    portinfoRef.innerHTML = ("This is port no. " + getCurrentPort())

  }
});


function makeBoxes(Howmany) {
  var square = ""
  var id = 0
  for (var i = 0; i < Howmany; i++) {
    console.log("Port " + i)
    // document.getElementById("switch-ports").insertAdjacentHTML("afterend", square)
    if (i % 7 === 6) {
      id = i + 1
      console.log("HEREEEE");
      square = "<div id='" + id + "' class='square' style='margin-left:15px;'></div>"
      document.getElementById("switch-ports").innerHTML += square;
    }
    else { 
      id = i + 1
      square = "<div id='" + id + "' class='square'></div>"
      document.getElementById("switch-ports").innerHTML += square;
    }
  }
}

function getURL() {
  alert("The URL of this page is: " + window.location.href );
}


async function httpCall(method, url, json_body) {

  (async () => {
    const rawResponse = await fetch(url, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: json_body
    });
    const content = await rawResponse.json();
  
    console.log(content);

    return content
  })();
}

// Get information about the switch from DNAC
async function fetchDNAC(){

  let url = 'https://198.18.133.101:443/dna/intent/api/v1/interface/network-device/1111bf67-8429-44be-be88-47d6e8b3259a'

  const response = await fetch(url, {
    method: 'GET',
    // body: myBody, // string or object
    mode: 'no-cors',
    headers: {
      'x-auth-token' : 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1ZmJmMGZiYWEwZTFjZTAwY2I5OTU3NGQiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVmYmYwZmI5YTBlMWNlMDBjYjk5NTc0YyJdLCJ0ZW5hbnRJZCI6IjVmYmYwZmI4YTBlMWNlMDBjYjk5NTc0YSIsImV4cCI6MTYzMTM0MTgxNiwiaWF0IjoxNjMxMzM4MjE2LCJqdGkiOiJiZjg5NmIxZS1kYWIzLTRlM2ItODYzNS1lOTM5MDliZjQxYjgiLCJ1c2VybmFtZSI6ImFkbWluIn0.vsLTh-I39BRzn3Ynw_S5WB1SBB1I_gqbi9un9kDw7UakaycfjcVulY47g9NeeTDHus1eoTAy62qi1E6WNcwSlD5pmFoQVX0I1d_omRLC_HysBONGHRoylxHYGqA9gRdFncEEJiw5jLk9tTK4VFJs3vJZREXOaIbrqK3K7Tl1ZQx4e7UGRIYRUO1x1OsekKUUr5sHp7i90eQu9XFQhl90P04zwrRQD_1m7FLZaBXtD1Xt_8bjnGAFPdVrlXlqoINh3yrceSohj8He8J7AKwbFf2XXWgCx8ZUN4JDX60bSufJ1mSRL-CzIlXWwfZDSso7RhGR8lGn5mvWtFqCnNzKtng',
      'content-type': 'application/json',
      'accept': 'application/json'
    }
  });

  console.log("API Call made here ....");

  const myJson = await response.json(); //extract JSON from the http response
  // do something with myJson

  // var obj = JSON.parse(myJson.response);

  console.log(myJson.response[0])

  // let mngmt_ip = myJson['46']

  // console.log(mngmt_ip);
  // console.log("Status: " + response.status);
}