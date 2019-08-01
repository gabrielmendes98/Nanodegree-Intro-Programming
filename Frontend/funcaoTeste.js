function getRelationship(x, y){
	if(isNaN(x) && !isNaN(y))
		return ("Can't compare relationships because " + x + " is not a number");
	else if(!isNaN(x) && isNaN(y))
		return ("Can't compare relationships because " + y + " is not a number");
	else if(isNaN(x) && isNaN(y))
		return ("Can't compare relationships because " + x + " and " + y + " are not numbers");
	else
		if(x>y)
			return (">");
		if(x<y)
			return ("<");
		return ("=");
}

function alphabetizer(names) {
	var i,j,menor,aux,menor2,pos;
    for(i = 0;i < names.length; i++){
    	names[i] = names[i].split(" ");
    	names[i] = names[i][1] + ", " + names[i][0];
    }
    
    for(i=0;i< names.length; i++){
    	menor = names[i];
    	for(j=i+1;j<names.length; j++){
    		menor2 = compara(menor,names[j]);
    		if(menor != menor2){
    			menor = menor2;
    			pos = j;
    			aux = names[i];
    			names[i] = menor2;
    			names[pos] = aux;
    		}
    	}
    }
	
    return names;
}

function compara(n1,n2){
	var i;
	for(i=0;i<n1.length && i<n2.length;i++){
		if(n1[i]<n2[i])
			return n1;
		if(n1[i]>n2[i])
			return n2;
	}
	return n1;
}

function ruleList(psiResults){
	var matrizString = [];
	for(var i in psiResults.formattedResults.ruleResults)
		matrizString.push(psiResults.formattedResults.ruleResults[i].localizedRuleName);
	return matrizString;
}

function totalBytes(psiResults){
	var soma = 0;
	for(var i in psiResults.pageStats){
		if(typeof(psiResults.pageStats[i]) == typeof ("a"))
			soma += parseInt(psiResults.pageStats[i]);
	}
	return soma;
}
