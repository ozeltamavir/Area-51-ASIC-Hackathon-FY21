window.addEventListener('load', function () {

  let switchports = document.querySelectorAll(".square");

  console.log(switchports)


  for (i = 0; i < switchports.length ; i++) {
      console.log(switchports[i])
      switchports[i].addEventListener('click', function(event) {
        alert('hey');
        button = event.target;
        button.classList.add("blueSquare");
      })

  }
});

