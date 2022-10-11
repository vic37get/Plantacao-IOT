function showMetricsData(metrica, limiar, alvo, classe1, classe2){
    if(metrica>=limiar){
        element = document.getElementById(alvo)
        element.setAttribute('class', classe1);
    }
    else{
        element = document.getElementById(alvo)
        element.setAttribute('class', classe2);
    }
}

function showBetterData(id, newDataPositive, newDataNegative){
    var target = document.getElementById(id).innerHTML;
    if (target == 1){
        document.getElementById(id).innerHTML = newDataPositive
    }
    else{
        target.innerHTML =  newDataNegative
        document.getElementById(id).innerHTML = newDataNegative
    }
}
