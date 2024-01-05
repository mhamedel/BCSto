
var zoneid,zonelabel;
var datnow = new Date(); 
var datbefor = new Date(datnow - 23 * 60 * 60 * 1000);
var daysOfWeek = ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam','Dim'];

var choiselect=1;
var dateselect=new Date();
var timestamp;
var NBpoint=24;
var lastDayOfMonth = new Date(dateselect.getFullYear(), dateselect.getMonth() + 1, 0);
var nbdaysMont=lastDayOfMonth.getDate();
var startOfWeek=new Date(dateselect);
startOfWeek.setDate(dateselect.getDate() - dateselect.getDay()); // Lundi de la semaine
var endOfWeek = new Date(dateselect);
endOfWeek.setDate(dateselect.getDate() - dateselect.getDay() + 6); // Dimanche de la semaine
var firstDayOfMonth= new Date(dateselect.getFullYear(), dateselect.getMonth(), 1);


function changedata(){
const date = new Date(document.getElementById('dateInput').value);
// let resultat = '';
  // Visualisation par heure
  dateselect = date;
  

  // Visualisation par jour sur une semaine
  startOfWeek = new Date(date);
  startOfWeek.setDate(date.getDate() - date.getDay()); // Lundi de la semaine
  endOfWeek = new Date(date);
  endOfWeek.setDate(date.getDate() - date.getDay() + 6); // Dimanche de la semaine


  // Visualisation par jour sur un mois
    firstDayOfMonth = new Date(date.getFullYear(), date.getMonth(), 1);

   lastDayOfMonth = new Date(date.getFullYear(), date.getMonth() + 1, 0);

   nbdaysMont=lastDayOfMonth.getDate();
   if(choiselect==3){
    NBpoint=nbdaysMont;}
  // resultat = `Visualisation de la température pour le mois de ${date.toLocaleString('default', { month: 'long' })} par jour`;

handleZoneClick(zoneid, zonelabel);
}


function checkPasswords() {
  var password = document.getElementById('password').value;
  var confirmPassword = document.getElementById('confirm_password').value;
  var passwordMatch = document.getElementById('passwordMatch');

  if (password === confirmPassword) {
      // Les mots de passe correspondent
      passwordMatch.style.display = 'none'; // Cache le message d'erreur s'il est affiché
      // alert('Les mots de passe correspondent!');
  } else {
      // Les mots de passe ne correspondent pas
      passwordMatch.style.display = 'block'; // Affiche le message d'erreur
      // alert('Les mots de passe ne correspondent pas!');
  }
}

$(document).ready(function () {

  var today = new Date().toISOString().split('T')[0];
  var dateInput = document.getElementById('dateInput');
  dateInput.value = today;




  $("#edithref").on("click", function () {
   
    $("#sectien_edite").show()
    $("#headTitel2").show()
    
    var alerdedit = document.getElementById('alerdedit');
    alerdedit.style.display = 'block'; 
    setTimeout(function() {alerdedit.style.display = 'none'; }, 5000);
    
    setTimeout(function() {
      $("#footer").show(); // Afficher l'élément #footer
  }, 1000); // Délai d'une seconde (1000 millisecondes)
    $("#headTitel").hide()
    $("#chars1").empty();
    $("#chars2").empty();
    $("#chars3").empty();
    $("#chars4").empty();
    

  });
  $("#info").on("click", function () {
    $(".pt-lg-112pt .nav-link").removeClass("active"); // Supprime la classe active de tous les liens
    $(this).addClass("active"); // Ajoute la classe active au lien cliqué
    
    $("#section_edit_info").show()
    $("#section_edit_Password").hide()
    $("#section_edit_parametre").hide()
  });
  $("#Password").on("click", function () {
    $(".pt-lg-112pt .nav-link").removeClass("active"); // Supprime la classe active de tous les liens
    $(this).addClass("active"); // Ajoute la classe active au lien cliqué
    
    $("#section_edit_info").hide()
    $("#section_edit_Password").show()
    $("#section_edit_parametre").hide()
    
  });
  $("#parametre").on("click", function () {
    $(".pt-lg-112pt .nav-link").removeClass("active"); // Supprime la classe active de tous les liens
    $(this).addClass("active"); // Ajoute la classe active au lien cliqué
    
    $("#section_edit_info").hide()
    $("#section_edit_Password").hide()
    $("#section_edit_parametre").show()
    
    
  });
  $("#zones").on("click", function () {
    // console.log("cklici zones ");
    var sidebarItems = $(this).children(".sidebar-menu-item");
    // console.log(" sidebarItems : ",sidebarItems.hasClass('open'));
    if (sidebarItems.hasClass("open")) {
      sidebarItems.removeClass("open");
    } else {
      sidebarItems.addClass("open");
    }
    // console.log(" sidebarItems : ",sidebarItems.hasClass('open'));
  });
  $("#select").on("click", function () {
    // console.log("cklici farms");
    var sidebarItems = $(this).children(".sidebar-menu-item");
    // console.log(" sidebarItems : ",sidebarItems);
    if (sidebarItems.hasClass("open")) {
      sidebarItems.removeClass("open");
    } else {
      sidebarItems.addClass("open");
    }
  });

  $("#farms").on("click", function () {
    // console.log("cklici farms");
    var sidebarItems = $(this).children(".sidebar-menu-item");
    // console.log(" sidebarItems : ",sidebarItems);
    if (sidebarItems.hasClass("open")) {
      sidebarItems.removeClass("open");
    } else {
      sidebarItems.addClass("open");
    }
  });

  $(document).on("click", ".sidebar-submenu", function () {
    
    if ($(this).data("farm-id")) {
      var farmid = $(this).data("farm-id");
      var farmlabel = $(this).find(".sidebar-menu-text").text();
      // console.log("data :", farmid, farmlabel);
      handleFarmClick(farmid, farmlabel);
    } else if ($(this).data("zone-id")) {
      // console.log("data :", $(this).data("zone-id"));

      zoneid = $(this).data("zone-id");
      zonelabel = $(this).find(".sidebar-menu-text").text();

      handleZoneClick(zoneid, zonelabel);
    }
    else if ($(this).data("select-id"))
     {
      choiselect=$(this).data("select-id")
      if(choiselect==1){NBpoint=24;}
      else if(choiselect==2){NBpoint=8;}
      else if(choiselect==3){NBpoint=nbdaysMont;}
      console.log("NBpoint ",NBpoint);
    
      handleZoneClick(zoneid, zonelabel);
      //APPEL ZONE 
    }

  });
});



//ajouter les zone
function handleFarmClick(farmId, farmlabel) {
  $("#footer").hide()
  // Faites ce que vous voulez avec le nom de la ferme
  // console.log("ID farm : " + farmId);
  // Vous pouvez appeler d'autres fonctions ou effectuer des actions supplémentaires ici
  $.ajax({
    type: "GET",
    url: "/web/get_zones", // Ajuster l'URL selon votre configuration
    data: { farm_id: farmId },
    success: function (data) {
      // Supprime tout le contenu actuel de l'élément Selecte "zones"
      $("#zones").empty();

      $("#label_farm").empty();
      $("#label_zone").empty();
      $("#label_farm").append(farmlabel);
      $("#chars1").empty();
      $("#chars2").empty();
      $("#chars3").empty();
      $("#chars4").empty();
      // console.log("data farm:", data);
      // Crée un nouvel élément de type <li>
      var zoneListItem = $(
        '<li class="sidebar-menu-item" >' +
          '<a class="sidebar-menu-button js-sidebar-collapse" data-toggle="collapse" >' +
          '<span class="material-icons sidebar-menu-icon sidebar-menu-icon--left">donut_large</span> Zones' +
          '<span class="ml-auto sidebar-menu-toggle-icon"></span>' +
          "</a>"
      );
      
      // Ajoute les options de zones renvoyées par le serveur
      for (var i = 0; i < data.length; i++) {
       
        zoneListItem.append('<ul class="sidebar-submenu collapse sm-indent" data-zone-id="' +
                      data[i].id + '"><li class="sidebar-menu-item"id="' +
                      data[i].name + '"><span class="sidebar-menu-button"> <span class="sidebar-menu-text">' +
                      data[i].label + '</span></span></li></ul>');
      }
      // Ajoute le nouvel élément <select> à l'élément Selecte "zones"
      $("#zones").append(zoneListItem);
      $("#zones").append("</li> ");

      zoneid=data[0].id;
      zonelabel=data[0].label;

      handleZoneClick(zoneid, zonelabel);
    },//end data success
    error: function ( status, error) {
       console.error("AJAX Error:", status, error);
    },
  });
  
  setTimeout(function() {
    $("#footer").show(); // Afficher l'élément #footer
}, 1000); // Délai d'une seconde (1000 millisecondes)
}


// creation chars
function handleZoneClick(zoneId, zonelabel) {
  $("#footer").hide()
  // console.log("Zones id :" + zoneId);
  $("#sectien_edite").hide()
  $("#headTitel2").hide()
  $("#headTitel").show()
  $("#chars1").empty();
  $("#chars2").empty();
  $("#chars3").empty();
  $("#chars4").empty();
  varst={    
     "zone_id": zoneId,
      "choiselect": choiselect,
      "firstDayOfMonth": firstDayOfMonth,
      "lastDayOfMonth": lastDayOfMonth,
      "startOfWeek": startOfWeek,
      "endOfWeek": endOfWeek,
      "dateselect":dateselect,
  }
  console.log(varst);
  $.ajax({
    type: "GET",
    url: "/web/get_sensor",
    data: { zone_id: zoneId,
       choiselect: choiselect,
       dateselect:dateselect,
       startOfWeek: startOfWeek,
       endOfWeek: endOfWeek,
       firstDayOfMonth: firstDayOfMonth,
      lastDayOfMonth: lastDayOfMonth,
       },
    success: function (dataresu) {
      
      $("#label_zone").empty();
      $("#label_zone").append(zonelabel);
      var min , max; 
      var minchar=0;
      var maxchar=45;       // par user
      var interval=5;
      var Unites={            //Unités de mesure
        "temperature":["°C","red","rgb(37, 236, 64)","rgb(37, 236, 200)",0,45,5],
        "humidity"   : ["%","red","rgb(37, 236, 64)","rgb(37, 236, 200)",0,100,10],
        "pH"         : ["","red","rgb(37, 236, 64)","rgb(37, 236, 200)",0,15,1],
        "salite"     : ["","red","rgb(37, 236, 64)","rgb(37, 236, 200)",0,40,5],
      }         
      console.log(dataresu)
      // for for 4 chans 4 section 
      // var s=0;
       var chans=Object.keys(dataresu[4]['data']);
       for (var m=0 ; m< chans.length; m++){
        var chan=chans[m];

      // recupere data et cree chart
      for (var j = 0; j < 4; j++) {
         
        var keys = Object.keys(dataresu[j])[0];
          max = dataresu[j][Object.keys(dataresu[j])[1]];
          min = dataresu[j][Object.keys(dataresu[j])[2]];
          minchar= Unites[keys][4];          
          maxchar= Unites[keys][5];          
          interval= Unites[keys][6];          
          console.log(keys)
        var selectElement = $(
          '<div class="row" style="height: 500px;"> <div class="col col-lg-3">'+
          '   <div style="padding: 30px; margin-top: 88px;"><p>'+
          keys+' :</p> </div>'+
          '</div><div class="col col-lg-9" > <div id="'+chan+'chartContainer' +
            j +
            '" style="height: 400px; width: 100%;"></div></div> </div>'
        );
        $("#chars"+chan).append(selectElement);
        
        var data_T = [];

            // creation data selent la T H PH S
        var ln = Object.keys(dataresu[4]['data'][chan]).length;
          for (var i = 0; i < ln; i++) {
              // odifier apre par data du controller  
             if(choiselect==1){   
                timestamp = new Date(dataresu[4]["data"][chan][i]["create_date"]); 
                datnow = new Date(dataresu[4]["data"][chan][0]["create_date"]);                                 //fin char X
                datbefor = new Date(dataresu[4]["data"][chan][ln-1]["create_date"]);    //debut char
              }
              else if(choiselect==2){
                timestamp = i;
                datnow = 7;                                           //fin char X
                datbefor = 0;                                         //debut char
              }
              else if(choiselect==3){
                datnow = NBpoint-1;                                 //fin char X
                datbefor = 0;  // debut char
                timestamp = i; 
              }
              if(j==0){data_T.push({
                x: timestamp,
                y: dataresu[4]["data"][chan][i]["MDR1"],
                });}
              else if(j==1){data_T.push({
                x: timestamp,
                y: dataresu[4]["data"][chan][i]["MDR2"],
                });}  
              else if(j==2){data_T.push({
                x: timestamp,
                y: dataresu[4]["data"][chan][i]["MDR3"],
                });}   
              else if(j==3){data_T.push({
                x: timestamp,
                y: dataresu[4]["data"][chan][i]["MDR4"],
                });}
                }   
    
       console.log(data_T)
        // semain ou jour ou mois 
        if(choiselect==1){
         var chart = new CanvasJS.Chart(chan+"chartContainer" + j, {
            animationEnabled: true,
            title: {
              // text: "date"
            },
            axisX:{
              valueFormatString:"HH:mm",
              minimum: datbefor,
              maximum: datnow,
              intervalType: "hour",
              // intervalType: "minute",
              interval:2,
              labelAngle: 0,
             },
            axisY: {
              maximum: maxchar,
              gridThickness: 0,
              minimum: minchar,
              interval: interval,
            },
            legend: {
              verticalAlign: "top",
              horizontalAlign: "right",
              dockInsidePlotArea: false,
            },
            data: [
              {
                name: "max",
                type: "area",
                borderWidth: 0,
                toolTipContent: null,
                color: Unites[keys][1],
                markerSize: 0,
                dataPoints: [
                  { x: datbefor, y: maxchar },
                  { x: datnow, y: maxchar },
                ],
              },
              {
                name: "center",
                type: "area",
                borderWidth: 0,
                toolTipContent: null,
                color: Unites[keys][2],
                markerSize: 0,
                dataPoints: [
                  { x: datbefor, y: max },
                  { x: datnow, y: max },
                ],
              },
              {
                name: "min",
                borderWidth: 0,
                toolTipContent: null,
                type: "area",
                color: Unites[keys][3],
                markerSize: 0,
                dataPoints: [
                  { x: datbefor, y: min },
                  { x: datnow, y: min },
                ],
              },
              {
                name: "",
                toolTipContent: "{y} "+Unites[keys][0],
                type: "spline",
                color: "rgba(0,75,141,0.7)",
                markerSize: 6,
                dataPoints: data_T,
              },
            ],
            backgroundColor: "#f5f7fa",
          }); // canvas char 1 creation end
        }
        else if(choiselect==2){
          var chart = new CanvasJS.Chart(chan+"chartContainer" + j, {
                    animationEnabled: true,
                    title: {
                      // text: "date"
                    },
                    axisX:{
					            labelFontSize: 13,
					            minimum: datbefor,
                      maximum: datnow,
                      interval:1,  
                      valueFormatString:"DDD",
                      tickLength: 0,
                      intervalType: "day", 
                      labelAngle: -170,
                      labelAutoFit: true, // Ajustement automatique
                      labelFormatter: function (e) {
                          return daysOfWeek[e.value];
                      }
                  },
                    axisY: {
                      maximum: maxchar,
                      gridThickness: 0,
                      minimum: minchar,
                      interval: interval,
                    },
                    legend: {
                      verticalAlign: "top",
                      horizontalAlign: "right",
                      dockInsidePlotArea: false,
                    },
                    data: [
                      {
                        name: "max",
                        type: "area",
                        borderWidth: 0,
                        toolTipContent: null,
                        color: Unites[keys][1],
                        markerSize: 0,
                        dataPoints: [
                          { x: datbefor, y: maxchar },
                          { x: datnow, y: maxchar },
                        ],
                      },
                      {
                        name: "center",
                        type: "area",
                        borderWidth: 0,
                        toolTipContent: null,
                        color: Unites[keys][2],
                        markerSize: 0,
                        dataPoints: [
                          { x: datbefor, y: max },
                          { x: datnow, y: max },
                        ],
                      },
                      {
                        name: "min",
                        borderWidth: 0,
                        toolTipContent: null,
                        type: "area",
                        color: Unites[keys][3],
                        markerSize: 0,
                        dataPoints: [
                          { x: datbefor, y: min },
                          { x: datnow, y: min },
                        ],
                      },
                      {
                        name: "",
                        toolTipContent: "{y} "+Unites[keys][0],
                        type: "spline",
                        color: "rgba(0,75,141,0.7)",
                        markerSize: 6,
                        dataPoints: data_T,
                      },
                    ],
                    backgroundColor: "#f5f7fa",
          }); // canvas char 2 creation end
        }
        else if(choiselect==3){
          var chart = new CanvasJS.Chart(chan+"chartContainer" + j, {
            animationEnabled: true,
            title: {
              // text: "date"
            },
            axisX:{
              minimum: datbefor,
              maximum: datnow,
              interval:1,  
              labelAngle: 0, 
              valueFormatString:"DDD",
              tickLength: 0,
              labelTextAlign: "left",
              labelFormatter: function (e) {
                return e.value + 1;
              }
          },
            axisY: {
              maximum: maxchar,
              gridThickness: 0,
              minimum: minchar,
              interval: interval,
            },
            legend: {
              verticalAlign: "top",
              horizontalAlign: "right",
              dockInsidePlotArea: false,
            },
            data: [
              {
                name: "max",
                type: "area",
                borderWidth: 0,
                toolTipContent: null,
                color: Unites[keys][1],
                markerSize: 0,
                dataPoints: [
                  { x: datbefor, y: maxchar },
                  { x: datnow, y: maxchar },
                ],
              },
              {
                name: "center",
                type: "area",
                borderWidth: 0,
                toolTipContent: null,
                color: Unites[keys][2],
                markerSize: 0,
                dataPoints: [
                  { x: datbefor, y: max },
                  { x: datnow, y: max },
                ],
              },
              {
                name: "min",
                borderWidth: 0,
                toolTipContent: null,
                type: "area",
                color: Unites[keys][3],
                markerSize: 0,
                dataPoints: [
                  { x: datbefor, y: min },
                  { x: datnow, y: min },
                ],
              },
              {
                name: "",
                toolTipContent: "{y} "+Unites[keys][0],
                type: "spline",
                color: "rgba(0,75,141,0.7)",
                markerSize: 6,
                dataPoints: data_T,
              },
            ],
            backgroundColor: "#f5f7fa",
          }); // canvas char 3 creation end
        }

        chart.render();
        unefoi=1;
      } //end for 4 chars
  
    }// end 4 chan

    },
    //success end
    error: function ( status, error) {
      console.error("AJAX Error:", status, error);
    }, // error end
  }); //ajax end
  $(".canvasjs-chart-credit").empty();
  
  setTimeout(function() {
    $("#footer").show(); // Afficher l'élément #footer
}, 1000); // Délai d'une seconde (1000 millisecondes)
} ///handleZoneClick end

