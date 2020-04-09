function getDate() {
    let today = new Date();
    let dd = today.getDate();
    let mm = today.getMonth()+1; //January is 0!
    let yyyy = today.getFullYear();
  
    if(dd<10) {
        dd = '0'+dd
    } 
  
    if(mm<10) {
        mm = '0'+mm
    } 
  
    today = yyyy + '-' + mm + '-' + dd;
    // let maxDate = today;
    // $('#inputdate').attr('max', maxDate);
    
    console.log(today);
    if(document.getElementById("inputdate").value ==''){
        document.getElementById("inputdate").value = today;
    }
    
    document.getElementById("inputdate").max = today;

  }
  
  
  window.onload = function() {
    getDate();
  };