function showMetricsData(metrica, limiar, alvo, classe1, classe2){
    if(metrica >= limiar){
        element = document.getElementById(alvo)
        element.setAttribute('class', classe1);
    }
    else{
        element = document.getElementById(alvo)
        element.setAttribute('class', classe2);
    }
}

function showMetricsDataForTerm(metrica, limiar, alvo, classe1, classe2){
    if(metrica == limiar){
        element = document.getElementById(alvo)
        element.setAttribute('class', classe1);
    }
    else{
        element = document.getElementById(alvo)
        element.setAttribute('class', classe2);
    }
}