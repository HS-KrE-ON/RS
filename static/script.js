// getting all required elements
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");
const del = searchWrapper.querySelector(".mark");
const icon = searchWrapper.querySelector(".icon");
const out1 = document.getElementById("output1");
const submit = searchWrapper.querySelector(".submit");
let linkTag = searchWrapper.querySelector("a");
var count = 0;
var clicks = 0;
let movies = [];
let res = [];

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
    //creating array list from user input
    showSuggestions(emptyArray);
    let allList = suggBox.querySelectorAll("li");
    for (let i = 0; i < allList.length; i++) {
      //adding onclick attribute in all li tags
      allList[i].setAttribute("onclick", "select(this)");
    }
  } else {
    searchWrapper.classList.remove("active"); //hide autocomplete box
  }
};

//delete input in searchbar pressing x-icon
del.onclick = () => {
  inputBox.value = "";
  searchWrapper.classList.remove("active"); //hide autocomplete box
};

//functions of the add-icon in searchbar
icon.onclick = () => {
  count++;
  let data = inputBox.value;
  if(inputBox.value == ""){
    return
    }
  //popup if a movie is already selected
  if(movies.includes(data)){
    inputBox.value = "";
    count = 0;
    window.open("#popup3", "_self");
  }
  //popup if wrong input (no possible movie)
  else if (!suggestions.includes(data)) {
    inputBox.value = "";
    count = 0;
    window.open("#popup2", "_self");
  } 
  else if(inputBox.value == ""){
    return
    }
  //generate selected movies list
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
  res = []; //resetting the recommendations if they are shown
  document.querySelector(".output1").innerHTML = `
  <ol>
  ${generateOutput(res)}
  </ol>
  `
  //autoscroll if selecting movies
  if(count==1 || count==3){document.getElementById("view1").scrollIntoView({behavior: 'smooth' });}
    //popup because of the limit of 5 movies
    } else {
      inputBox.value = "";
      count = 0;
      window.open("#popup1", "_self");
    }
  }
  searchWrapper.classList.remove("active"); //hide autocomplete box
};

//select the input movie
function select(element) {
  let selectData = element.textContent;
  inputBox.value = selectData;
  searchWrapper.classList.remove("active"); //hide autocomplete box
  //popup if wrong input (no possible movie)
  if (!suggestions.includes(selectData)) {
    inputBox.value = "";
    count = 0;
    window.open("#popup2", "_self");
  }
}

//creating array list from user input
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

//generate the selected movies list with remove icons
function generateListItems(arg) {
  let items = "";
  for (let i = 0; i < arg.length; i++) {
    items += `<li id="item">${arg[i]}<input type="button" value="X" id="${[
      i,
    ]}" onclick="remove(this)"></li>`; //possibility to remove a movie
  }
  return items;
}

//generate the recommended movies list
function generateOutput(arg) {
  let items = "";
  for (let i = 0; i < arg.length; i++) {
    items += `<li id="item">${arg[i]}</li>`;
  }
  return items;
}

//remove a movie from the selected movies list when pressed the remove icon
function remove(element) {
  var value = element.id;
  console.log("Gelöschtes Element: " + value);
  movies.splice(value, 1);
  console.log(movies);
  //generate a new list without the removed movie
  document.querySelector(".output").innerHTML = `
  <ol>
  ${generateListItems(movies)}
  </ol>
  `;
  res = []; //resetting the recommendations if they are shown
  document.querySelector(".output1").innerHTML = `
  <ol>
  ${generateOutput(res)}
  </ol>
  `;
}

//submit the selected movies and get the recommendations from backend
function submitMovies() {
  clicks ++;
  // only one click is possible
  if (clicks > 1){
    return
  }
  else{
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
      element = document.getElementById("view").scrollIntoView({behavior: 'smooth' });
      clicks = 0;
    },
  });
}
}

//clear the page
function clear_all() {
  movies = [];
  res = [];
  count = 0;
  //clear the selected movies list
  document.querySelector(".output").innerHTML = `
  <ol>
  ${generateListItems(movies)}
  </ol>
  `;
  //clear the recommended movies list
  document.querySelector(".output1").innerHTML = `
      <ol>
      ${generateOutput(res)}
      </ol>
      `;
}