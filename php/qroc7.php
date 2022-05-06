<?php


$con=mysqli_connect("localhost","root","", "crdb2" );  //db변경
mysqli_set_charset($con,"utf8"); 
$sql="select * from totaloffer"; //db변경
$result=mysqli_query($con,$sql);
$data = array();

if($result){
   
   while($row=mysqli_fetch_array($result)){
       array_push($data, 
           array('id'=>$row[0],
           'title'=>$row[1],
           'datedue'=>$row[2]
        ));
    }

   header('Content-Type: application/json; charset=utf8');
    $json = json_encode(array("webnautes"=>$data), JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
    echo $json;

}

mysqli_close($con);  
    

?>