function applyChanges(){
    var color = document.getElementById('color').value;
    var changes1 = document.getElementsByName("col")
    var changes2 = document.getElementsByName("b-col")
    for( var i = 0; i < changes1.length; i++ ){
        changes1[i].style.color=color;
    }
    for( var i = 0; i < changes2.length; i++ ){
        changes2[i].style.backgroundColor=color;
    }
}
        