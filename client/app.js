    function onClickedEstimatedStressLevel() {
    console.log("Estimate Stress Level button clicked");
    var humidity = parseFloat(document.getElementById("humidity").value);
    var temperature = parseFloat(document.getElementById("temperature").value);
    var step_count = parseInt(document.getElementById("step_count").value);
    var estStressLevel = document.getElementById("uiEstimatedStressLevel");
  
    // var url = "http://127.0.0.1:5000/predict_stress_level"; //Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/api/predict_stress_level"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        humidity: humidity,
        temperature: temperature,
        step_count: step_count
    }, function(data, status) {
        // Log the response
        console.log(data.estimated_stress_level);
        // Update the UI with the estimated stress level
        estStressLevel.innerHTML = "<h2>" + data.estimated_stress_level.toString() + " </h2>";
        // Log the status of the request
        console.log(status);
    });
}
function onPageLoad() {
    console.log("Page loaded");
    // Add any additional initialization code here
}
  
  
  window.onload = onPageLoad;