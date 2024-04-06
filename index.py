<html>
    <head>
        <title>Pico W Multimeter</title>

        <style>
            *{
               font-family: sans-serif;
             }
            
             table.GeneratedTable {
               width: 30%;
               background-color: 口#ffffff;
               border-collapse: collapse;
               border-width: 2px;
               border-color: #000000;
               border-style: solid;
               color: 口#000000;
             }
             
             table.GeneratedTable td, table. GeneratedTable th {
             border-width: 2px;
             border-color: 口#000000;
             border-style: solid;
             padding: 3px;
            }
             
            table.GeneratedTable thead {
              background-color: #00aaff;
            }
        </style>
    </head>
    
    
    <body>
        <hl>Pico W Multimeter</h1>
        
        <table class="GeneratedTable"> 
          <thead>
            <tr>
              <th style="width: 60%;">Reading</th>
              <th style="width: 40%;">Value</th>
            </tr>
         </thead>
         <tbody>
           <tr>
             <td>voltage</td>
             <td><div id="voltage"></div>V</td>
           </tr>
           <tr>
             <td>Current</td>
             <td><div id="current"></div>mA</td>
           </tr>
         </tbody>
       </table>
       
       <div id="content2"></div>
   </body>
</html> 
<script src="//code.jquery.com/jquery-1.10.2.js"></script>
<script>
function loadDoc() {
const xhttp = new XMLHttpRequest();
xhttp.onload = function()
{
values = this.responseText.split(":");
document.getElementById("voltage").innerHTML = values[0l;
document.getElementById("current").innerHTML = values[1]
 }                                                     
xhttp.open("GET", "get-readings");
xhttp.send();
}
setInterval(function()
 {           
loadDoc();
}, 500); 
</script>
<!-- CSS Code: place this code in the document's head (between the'head' tags) -->
 <style>