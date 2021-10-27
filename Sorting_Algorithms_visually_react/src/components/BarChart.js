import * as React from "react";
import {Bar} from 'react-chartjs-2'



class Chart extends React.Component{
    constructor(props){
        super(props);
        this.chartReference = React.createRef();
        this.state = {
            chartData: props.chartData
        }
        this.changeData = this.changeData.bind(this) 
    }
    changeData = (newDataState) =>{
        this.setState({
            chartData: newDataState
        });
        // console.count(
        //     'The change Data has been ran:  ' 
        //   )
        this.reference.update();
        //console.log("CHART State Data: "+ this.state.chartData.labels);
    }

    render(){
        return(
            <div className="chart">
                <Bar
                    ref = {(reference) => this.reference = reference}
                    data={this.state.chartData}
                    width={600}
                    height={400}
                    options={{ responsive: true, maintainAspectRatio: false }}
                />
            </div>
        )
    }
}
export default Chart;


// const Barchart = (ref, data, labels) => {
//     //Try to take Data out of the Bar constructor   
//     return(
//         <div>
//             <Bar
//             data = {{
//                 labels: labels, 
//                 datasets: [
//                     {
//                         label:'A randomly generated number entry',
//                         data: data,
//                         backgroundColor: 'purple'
//                     },
//                 ],
//             }}
//             height={400}
//             width ={600}
//             options={{
//                 skipLabels : true,
//                 maintainAspectRatio : false,
//                 scales: {
//                     yAxes: [
//                         {
//                         ticks: {
//                             beginAtZero : true,
//                         }, 
//                     }    
//                 ],
//             },
//         }}
//         />
//         </div>
//     )
// }

// const ReturnArrayToSort = () =>{
//     return arrayToSort;
// }
// export default Barchart

// var BSbutton = document.createElement("BSbutton");
// BSbutton.innerHTML = "BubbleSort";

// // 2. Append somewhere
// var body = document.getElementsByTagName("body")[0];
// body.appendChild(BSbutton);

// // 3. Add event handler
// BSbutton.addEventListener ("click", function() {
//   alert("Running Bubble Sort");
//   BubbleSort(arrayToSort);
// });