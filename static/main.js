const button = document.getElementById('btn') 
// const score = document.querySelector('#display_image2')

var uploaded_image

var body

var file

var image2

// var image = new Image();


// function marks_update() {

//     console.log("run")

//     var chr = new XMLHttpRequest()
//     chr.open('GET', './static/json/marks.json', true)

//     chr.onload = function() {
//         var mark = JSON.parse(this.responseText)

//         console.log(mark['marks'])

//         document.getElementById('score').innerHTML = mark['marks']
//     }

//     chr.send()
// }

const image_input = document.querySelector("#image_input");
image_input.addEventListener("change", function() {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
    uploaded_image = reader.result;
    console.log(typeof uploaded_image)
    console.log(uploaded_image)
    document.querySelector("#display_image").style.backgroundImage = `url(${uploaded_image})`;
});
    reader.readAsDataURL(this.files[0]);
});

// function api_call(){

//     var body2 = JSON.stringify(body)

//     var vhr = new XMLHttpRequest();
//     vhr.open('POST', '/', true);

//     vhr.setRequestHeader('Content-Type', 'application/json')

//     vhr.send(body2)

//     const myTimeout = setTimeout(marks_update, 10000)

//   }


async function api_call(){
    const api_response = await fetch(`/mirnet-api`,
     { method: 'POST', 
     body: JSON.stringify(body), 
     headers: { 'Content-Type': 'application/json',
     mode: 'no-cors' }})
    const response = await api_response.json()

    return response
  }

function toDataUrl(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.onload = function() {
        var reader = new FileReader();
        reader.onloadend = function() {
            callback(reader.result);
        }
        reader.readAsDataURL(xhr.response);
    };
    xhr.open('GET', url);
    xhr.responseType = 'blob';
    xhr.send();
}

function base() {
    var base64 = "base"
        toDataUrl(uploaded_image , function(myBase64) {
        console.log(myBase64); // myBase64 is the base64 string

        base64 = myBase64

        const base64_split = base64.split(",")[1]
        console.log(base64_split)
    
        body = {
            "png": base64_split
        }

        api_call().then(resp => 
            update_refined_image(resp)
    
        )
    
    })}

button.addEventListener('click', upload)

function upload() {

    base()

}



function dataURLtoFile(dataurl, filename) {
 
    var arr = dataurl.split(','),
        // mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]), 
        n = bstr.length, 
        u8arr = new Uint8Array(n);
        
    while(n--){
        u8arr[n] = bstr.charCodeAt(n);
    }
    
    return new File([u8arr], filename, {type:mime});
}

function update_refined_image(response) {
    image2 = response['refined_image']
    console.log(image2)
    document.querySelector("#display_image2").style.backgroundImage = `url(${image2})`
}