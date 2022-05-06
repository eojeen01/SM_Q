<?php

$con = mysqli_connect('localhost', 'root', '', 'crdb2');

if(!$con)
{
    echo "데이터베이스 접속 에러 : ";
    echo mysqli_connect_error();
    exit();
}

mysqli_set_charset($con, "utf8");
$sql = "select * from totaloffer";
$res1 = mysqli_query($con, $sql);
$res2 = array();

if($res1){
    while($row = mysqli_fetch_array($res1)) {
        array_push($res2,
            array('id'=>$row[0], 'title'=>$row[1], 'due'=>$row[2] 
            ));
    }

    echo json_encode(array('crawlingResult'=>$res2));
}

else{
    echo "SQL문 처리중 에러 발생 : ";
    echo mysqli_error($con);
}


mysqli_close($con);
?>