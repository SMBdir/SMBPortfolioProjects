
import React from 'react'
import {Bar} from 'react-chartjs-2'
import Button from './Button'
import App from '../App';
import {UpdateBarChart} from '../App'

var arrayToSort;
var labels
const Barchart = () => {
    arrayToSort = [500];
    labels = [500]
    for(let i=0; i<500; i++){
        let nextNum = Math.floor(Math.random() * 1000);
        arrayToSort[i] = nextNum;
        labels[i] = ''
    }
    labels[0] = 'Lowest'
    labels[495] = 'Highest'

    //Try to take Data out of the Bar constructor   

    return(
        <div>
            <Bar
            data = {{
                labels: labels, 
                datasets: [
                    {
                        label:'A randomly generated number entry',
                        data: arrayToSort,
                        backgroundColor: 'purple'
                    },
                ],
            }}
            height={400}
            width ={600}
            options={{
                skipLabels : true,
                maintainAspectRatio : false,
                scales: {
                    yAxes: [
                        {
                        ticks: {
                            beginAtZero : true,
                        }, 
                    }    
                ],
            },
        }}
        />
        </div>
    )
}

const ReturnArrayToSort = () =>{
    return arrayToSort;
}
export default Barchart

var BSbutton = document.createElement("BSbutton");
BSbutton.innerHTML = "BubbleSort";

// 2. Append somewhere
var body = document.getElementsByTagName("body")[0];
body.appendChild(BSbutton);

// 3. Add event handler
BSbutton.addEventListener ("click", function() {
  alert("Running Bubble Sort");
  BubbleSort(arrayToSort);
});


function BubbleSort(arrayToSort){
    //var length = arrayToSort.length;

    var swappedOnCurrentIter = false;
    var placeholder;

     for (let i=1; i<500; i++){
         if(arrayToSort[i-1]>arrayToSort[i]){
            placeholder = arrayToSort[i-1];
            arrayToSort[i-1] = arrayToSort[i];
            arrayToSort[i] = placeholder;
            swappedOnCurrentIter = true; 
         }
    }
    if(swappedOnCurrentIter == true){
        UpdateBarChart(arrayToSort);
        BubbleSort(arrayToSort);
    }
    else{
        return arrayToSort;
    }
}
