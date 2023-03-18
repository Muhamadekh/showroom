// $(document).ready(function(){
//     $("#searchBox").on("input", function(e){
//         textInSearchBox = $("#searchBox").val();
//         $.ajax({
//             method: "post",
//             url: "/livesearch",
//             data: {text:textInSearchBox},
//             success:function(res){
//                 console.log(res);
//             }
//             }
//
//         )
//     });
// })

const getData = (url,methods,data,handle) => {
   fetch(url,{
     method: methods,
     headers: {
       'Accept': 'application/json',
       'Content-Type': 'application/json'
     },
     body: JSON.stringify(data)
   })
   .then(res=>res.json())
   .then(res => handle(res));
  };
$("#searchBox").on("input",(e)=>{
   let search_term = $("#searchBox").val()
    let cars_div = $("#cars_results")
    cars_div.html("")
    getData(`http://${window.location.hostname}:5000/livesearch`,"POST",{"text" : search_term},(data)=>{
    let cars_searched = "";
        for (let i = 0; i < data.length; i++) {
            cars_searched+= `<div class="col-sm">
                  <div class="card">
                      <img class="card-img-top img-thumbnail" src="${data[i].photo}">
                      <div class="card-body">
                        <h5 class="card-title">Type: ${data[i].name}<h6 class="card-text">Price: ${data[i].price}
                        <span class="dot"></span>Mileage: ${data[i].mileage}</h6></h5>
                        <a href="#" class="btn btn-primary">Learn More</a>
                      </div>
                  </div>
            </div>`

        }
    cars_div.html(cars_searched)
})})
