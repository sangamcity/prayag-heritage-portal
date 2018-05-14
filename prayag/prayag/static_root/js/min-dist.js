// This example requires the Places library. Include the libraries=places 
var dstMatrix = []; 
var path = []; 
var N; 
$(document).ready(function() { 
  $("#route_btn").click(function(event) { 
    var src = $("[name='src']").val(); 
    var dst = []; 
    dst.push(src); 
    $.each($('input[name="dst"]:checked'), function() { 
      dst.push($(this).val()); 
    }); 
    dstMatrix.push([0, 0]); 
    for (var i = 0; i < dst.length; i++) { 
      var temp = []; 
      temp.push(0); 
      for(var j = 0; j < dst.length; j++){ 
        temp = getDistance(dst[i], dst[j], temp); 
      } 
      console.log(temp); 
      dstMatrix.push(temp); 
    } 
    N = dst.length; 
    getOptimalPath(); 
  }); 
}); 
var dp = []; 
var MAX = 10000000000; 
function rec(n, count){ 
  console.log(dstMatrix[1][0]); 
  if(count == ((1<<N) - 1)) return 0; 
  if(dp[n][count] != -1) return dp[n][count]; 
  count  = count | ((1<<N)-1); 
  var ans = MAX; 
  var pos = -1; 
  for(var i = 1; i <= n; i++){ 
        if((count & (1<<(i-1))) == 0){ 
            var tmp = dstMatrix[n][i] + rec(i, count | (1<<(i-1))); 
            if(tmp < ans){ 
                ans = tmp; 
                pos = i; 
            } 
        } 
    } 
    if(pos != -1) 
        path.push(pos); 
    return dp[n][count] = ans; 
}  
function getOptimalPath(){ 
    for(var i = 0; i <25; i++){ 
      var temp = []; 
      for(var j = 0; j < 25; j++){ 
        temp.push(-1); 
      } 
      dp.push(temp); 
    } 
    ans = rec(1, 1); 
    alert(ans); 
    path.push(1); 
    path.reverse(); 
} 
function convert(dist_str) { 
  var d = dist_str.split(" "); 
  var ans = parseFloat(d[0]); 
  if (d[1] == "km") 
    ans *= 1000.0; 
  return ans; 
} 
 
function getDistance(src ,dst, temp) { 
  //*********DISTANCE AND DURATION**********************// 
  service = new google.maps.DistanceMatrixService(); 
  service.getDistanceMatrix({ 
    origins: [src], 
    destinations: [dst], 
    travelMode: 'DRIVING', 
    unitSystem: google.maps.UnitSystem.METRIC, 
    avoidHighways: false, 
    avoidTolls: false 
  }, function(response, status) { 
      if (status == google.maps.DistanceMatrixStatus.OK && response.rows[0].elements[0].status != "ZERO_RESULTS") { 
      distance = response.rows[0].elements[0].distance.text; 
      temp.push(convert(distance)); 
    } else { 
      alert("Unable to find the distance."); 
    } 
  }); 
  return temp; 
};