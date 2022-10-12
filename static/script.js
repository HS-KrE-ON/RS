// getting all required elements
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");
const del = searchWrapper.querySelector(".mark");
const icon = searchWrapper.querySelector(".icon");
const out1 = document.getElementById("output1");
const submit = searchWrapper.querySelector(".submit");
let linkTag = searchWrapper.querySelector("a");
let movies = [];
let count = 0;

// if user press any key and release
inputBox.onkeyup = (e) => {
  let userData = e.target.value; //user enetered data
  let emptyArray = [];
  if (userData) {
    emptyArray = suggestions.filter((data) => {
      //filtering array value and user characters to lowercase and return only those words which are start with user enetered chars
      return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
    });
    emptyArray = emptyArray.map((data) => {
      // passing return data inside li tag
      return (data = `<li>${data}</li>`);
    });
    searchWrapper.classList.add("active"); //show autocomplete box
    showSuggestions(emptyArray);
    let allList = suggBox.querySelectorAll("li");
    for (let i = 0; i < allList.length; i++) {
      //adding onclick attribute in all li tag
      allList[i].setAttribute("onclick", "select(this)");
    }
  } else {
    searchWrapper.classList.remove("active"); //hide autocomplete box
  }
};

del.onclick = () => {
  inputBox.value = "";
};

icon.onclick = () => {
  let data = inputBox.value;
  if (!suggestions.includes(data)) {
    inputBox.value = "";
    window.open("#popup2", "_self");
  } 
  else if(movies.includes(data)){
    inputBox.value = "";
    window.open("#popup3", "_self");
  }
  else if(inputBox.value == ""){
    break
  }
  else {
    if (movies.length < 5) {
      movies.push(data);
      console.log(movies);
      inputBox.value = "";
      document.querySelector(".output").innerHTML = `
  <ol>
  ${generateListItems(movies)}
  </ol>
  `;
    } else {
      inputBox.value = "";
      window.open("#popup1", "_self");
    }
  }
  searchWrapper.classList.remove("active");
};

function select(element) {
  let selectData = element.textContent;
  inputBox.value = selectData;
  searchWrapper.classList.remove("active");
  if (!suggestions.includes(selectData)) {
    inputBox.value = "";
    window.open("#popup2", "_self");
  }
}

function showSuggestions(list) {
  let listData;
  if (!list.length) {
    userValue = inputBox.value;
    listData = `<li>${userValue}</li>`;
  } else {
    listData = list.join("");
  }
  suggBox.innerHTML = listData;
}

function generateListItems(arg) {
  let items = "";
  for (let i = 0; i < arg.length; i++) {
    items += `<li id="item">${arg[i]}<input type="button" value="X" id="${[
      i,
    ]}" onclick="remove(this)"></li>`;
  }
  return items;
}

function generateOutput(arg) {
  let items = "";
  for (let i = 0; i < arg.length; i++) {
    items += `<li id="item">${arg[i]}</li>`;
  }
  return items;
}

function remove(element) {
  var value = element.id;
  console.log("Gelöschtes Element: " + value);
  movies.splice(value, 1);
  console.log(movies);
  document.querySelector(".output").innerHTML = `
  <ol>
  ${generateListItems(movies)}
  </ol>
  `;
}

function submitMovies() {
  $.ajax({
    url: "post",
    type: "POST",
    data: {
      moviearr: movies,
    },
    success: function (res) {
      console.log("Flask input " + res);
      document.querySelector(".output1").innerHTML = `
      <ol>
      ${generateOutput(res)}
      </ol>
      `;
    },
  });
}

function clear_all() {
  movies = [];
  res = []
  document.querySelector(".output").innerHTML = `
  <ol>
  ${generateListItems(movies)}
  </ol>
  `;
  document.querySelector(".output1").innerHTML = `
      <ol>
      ${generateOutput(res)}
      </ol>
      `;
}