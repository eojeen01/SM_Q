<?php

$con = mysqli_connect('localhost', 'root', '', 'crdb2');


if(!$con)
{
    echo "데이터베이스 접속 에러 : ";
    echo mysqli_connect_error();
    exit();
}

mysqli_set_charset($con, "utf8");
$sql1 = "insert into engioffer select * from totaloffer where title like '%SW%' or title like '%ICT%' or title like '%공대%' or title like '%공학%'";
$res1 = mysqli_query($con, $sql1);
$sql2 = "select * from engioffer";
$res2 =  mysqli_query($con, $sql2);
$res3 = array();

if($res2){
    while($row = mysqli_fetch_array($res2)) {
        array_push($res3,
            array('id'=>$row[0], 'title'=>$row[1], 'due'=>$row[2] 
            ));
    }

    echo json_encode(array('crawlingResult'=>$res3));
}

else{
    echo "SQL문 처리중 에러 발생 : ";
    echo mysqli_error($con);
}


mysqli_close($con);
?>