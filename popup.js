window.addEventListener('load', function () {

  chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
    console.log(url);
    // use `url` here inside the callback because it's asynchronous!
  });

  let switchports = document.querySelectorAll(".square");

  console.log(switchports)


  for (i = 0; i < switchports.length ; i++) {
      console.log(switchports[i])
      switchports[i].addEventListener('click', function(event) {
        alert('hey');
        button = event.target;
        button.classList.add("blueSquare");

        fetch("http://127.0.0.1:8008/", {method: "POST", body: JSON.stringify("Test data")});
      })

  }
});