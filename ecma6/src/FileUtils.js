/**
 * Created by gcharles on 10/11/16.
 */
function readEulerDataFile(fileName) {
    let allText = null;
    let rawFile = new XMLHttpRequest();

    rawFile.open("GET", `http://localhost:63343/ecma6/data/${fileName}`, false);
    //rawFile.open("GET", `http://projecteuler.net/project/resources/${fileName}`, false);
    rawFile.onreadystatechange = function () {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                allText = rawFile.responseText;
            }
        }
    };
    rawFile.send(null);
    return allText;
}