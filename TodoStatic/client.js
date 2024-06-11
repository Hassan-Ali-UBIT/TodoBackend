const formEl = document.querySelector("#login-form");
formEl?.addEventListener("submit", (e) => {
  e.preventDefault();
  let data = new FormData(formEl);
  let dataObj = Object.fromEntries(data);
  let strObj = JSON.stringify(dataObj);
  let base_url = "http://127.0.0.1:8000/api/";
  let auth_url = base_url + "token/";
  let refresh_url = auth_url + "refresh/";
  let verify_url = auth_url + "verify/";
  let todos_url = base_url + "todos/";
  let auth_option = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: "",
  };
  let get_option = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: "",
    },
  };
  let accessToken = localStorage.getItem("accessToken") || 0;
  let refreshToken = localStorage.getItem("refreshToken") || 0;

  if (accessToken != 0) {
    auth_option.headers.Authorization = `Bearer ${accessToken}`;
    auth_option.body = JSON.stringify({ token: accessToken });

    fetch(verify_url, auth_option)
      .then((res) => {
        console.log(res.status);
        if (res.status == 401 || res.status == 403) {
          auth_option.body = JSON.stringify({ refresh: refreshToken });

          fetch(refresh_url, auth_option)
            .then((res) => res.json())
            .then((res) => {
              if (res.status == 200) {
                localStorage.setItem("accessToken", res["access"]);
                get_option.headers["Authorization"] = `Bearer ${res["access"]}`;

                fetch(todos_url, get_option)
                  .then((res) => res.json())
                  .then((res) => console.log(res));
              } else {
                auth_option.body = strObj;
                fetch(auth_url, auth_option)
                  .then((res) => {
                    return res.json();
                  })
                  .then((res) => {
                    localStorage.setItem("accessToken", res["access"]);
                    localStorage.setItem("refreshToken", res["refresh"]);

                    get_option.headers[
                      "Authorization"
                    ] = `Bearer ${res["access"]}`;

                    fetch(todos_url, get_option)
                      .then((res) => res.json())
                      .then((res) => console.log(res));
                  });
              }
            })
            .catch((err) => console.log(err));
        } else {
          get_option.headers["Authorization"] = `Bearer ${accessToken}`;

          fetch(todos_url, get_option)
            .then((res) => res.json())
            .then((res) => console.log(res));
        }
      })
      .catch((err) => console.log(err));
  } else {
    auth_option.body = strObj;
    fetch(auth_url, auth_option)
      .then((res) => {
        return res.json();
      })
      .then((res) => {
        localStorage.setItem("accessToken", res["access"]);
        localStorage.setItem("refreshToken", res["refresh"]);

        get_option.headers["Authorization"] = `Bearer ${res["access"]}`;

        fetch(todos_url, get_option)
          .then((res) => res.json())
          .then((res) => console.log(res));
      });
  }
});
