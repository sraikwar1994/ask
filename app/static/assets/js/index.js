function loadTable() {
  const xhttp = new XMLHttpRequest();
  xhttp.open("GET", "/api/users/");
  xhttp.send();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log(this.responseText);
      var trHTML = ''; 
      const objects = JSON.parse(this.responseText);
      for (let object of objects) {
        trHTML += '<tr>'; 
        trHTML += '<td>'+object['id']+'</td>';
        trHTML += '<td>'+object['firstname']+'</td>';
        trHTML += '<td>'+object['lastname']+'</td>';
        trHTML += '<td>'+object['username']+'</td>';
        trHTML += '<td><button type="button" class="btn btn-outline-secondary mx-2" onclick="showUserEditBox('+object['id']+')">Edit</button>';
        trHTML += '<button type="button" class="btn btn-outline-danger" onclick="userDelete('+object['id']+')">Del</button></td>';
        trHTML += "</tr>";
      }
      document.getElementById("mytable").innerHTML = trHTML;
    }
  };
}

loadTable();

function showUserCreateBox() {
  Swal.fire({
    title: 'Create user',
    html:
      '<input id="id" type="hidden">' +
      '<input id="firstname" class="swal2-input" placeholder="First">' +
      '<input id="lastname" class="swal2-input" placeholder="Last">' +
      '<input id="username" class="swal2-input" placeholder="Username">' +
      '<input id="email" class="swal2-input" placeholder="Email">',
    focusConfirm: false,
    preConfirm: () => {
      userCreate();
      loadTable();
    }
  })
}

function userCreate() {
  const firstname = document.getElementById("firstname").value;
  const lastname = document.getElementById("lastname").value;
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
    
  const xhttp = new XMLHttpRequest();
  xhttp.open("POST", "/api/users/create/");
  xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhttp.send(JSON.stringify({ 
    "firstname": firstname, "lastname": lastname, "username": username, "email": email,
  }));
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      const objects = JSON.parse(this.responseText);
      Swal.fire(objects['message']);
      loadTable();
    }
  };
}

function userDelete(id) {
  const xhttp = new XMLHttpRequest();
  xhttp.open("DELETE", "/api/users/delete/");
  xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhttp.send(JSON.stringify({ 
    "id": id
  }));
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4) {
      const objects = JSON.parse(this.responseText);
      Swal.fire(objects['message']);
      loadTable();
    } 
  };
}

function showUserEditBox(id) {
  console.log(id);
  const xhttp = new XMLHttpRequest();
  xhttp.open("GET", "/api/users/"+id);
  xhttp.send();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      const user = JSON.parse(this.responseText);
      console.log(user);
      Swal.fire({
        title: 'Edit User',
        html:
          '<input id="id" type="hidden" value='+user['id']+'>' +
          '<input id="firstname" class="swal2-input" placeholder="First" value="'+user['firstname']+'">' +
          '<input id="lastname" class="swal2-input" placeholder="Last" value="'+user['lastname']+'">' +
          '<input id="username" class="swal2-input" placeholder="Username" value="'+user['username']+'">' +
          '<input id="email" class="swal2-input" placeholder="Email" value="'+user['email']+'">',
        focusConfirm: false,
        preConfirm: () => {
          userEdit();
        }
      })
    }
  };
}

function userEdit() {
  const id = document.getElementById("id").value;
  const firstname = document.getElementById("firstname").value;
  const lastname = document.getElementById("lastname").value;
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
    
  const xhttp = new XMLHttpRequest();
  xhttp.open("PUT", "/api/users/update/");
  xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhttp.send(JSON.stringify({ 
    "id": id, "firstname": firstname, "lastname": lastname, "username": username, "email": email,
  }));
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      const objects = JSON.parse(this.responseText);
      Swal.fire(objects['message']);
      loadTable();
    }
  };
}
