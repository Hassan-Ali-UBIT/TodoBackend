const formEl = document.querySelector("#login-form");
formEl?.addEventListener("submit", (e) => {
  e.preventDefault();
  let data = new FormData(formEl);
  let dataObj = Object.fromEntries(data);
  let strObj = JSON.stringify(dataObj);
  let base_url = "http://127.0.0.1:8000/api/";
  let auth_url = base_url + "token/";
  let refresh_url = base_url + "refresh/";
  let todos_url = base_url + "todos/";

  fetch(auth_url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: strObj,
  })
    .then((res) => {
      return res.json();
    })
    .then((res) => {
      let access = res["access"];
      let refresh = res["refresh"];

      fetch(todos_url, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${access}`,
        },
      })
        .then((res) => {
          return res.json();
        })
        .then((res) => {
          console.log(res);
        });
    })
    .catch((err) => {
      console.log(err);
    });
});
