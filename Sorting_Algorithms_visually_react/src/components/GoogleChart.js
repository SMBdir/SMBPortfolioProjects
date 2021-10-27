import * as React from "react";
import { Chart } from "react-google-charts";


class GoogleChart extends React.Component{
    constructor(props){
        super(props);
        this.chartReference = React.createRef();
        this.state = {
            arrayToSort: props.arrayToSort,
            chartData: props.chartData
        }

    }
    UNSAFE_componentWillMount(){
        this.getChartData();
      }
    
    ResetToRandom(){
        let arrayToSort = [500];
        for(let i=0; i<500; i++){
          let nextNum = Math.floor(Math.random() * 1000);
          arrayToSort[i] = nextNum;
        }
        console.log("START", arrayToSort);
        return arrayToSort;
      }
    
    ResetOnclick(){
        let newRandomArray = this.ResetToRandom();
        this.UpdateBarChart(newRandomArray);
    }
    
     BubbleSort = (passedArrayToSort) =>{
        let arrayToSort = passedArrayToSort;
        console.log("bubble: ", arrayToSort)
        var swappedOnCurrentIter = false;
        var placeholder;
        let newArray = arrayToSort;
    
         for (let i=1; i<500; i++){
             if(newArray[i-1]>newArray[i]){
                placeholder = newArray[i-1];
                newArray[i-1] = newArray[i];
                newArray[i] = placeholder;
                swappedOnCurrentIter = true; 
             }
        }
        if(swappedOnCurrentIter === true){
          this.UpdateBarChart(newArray);
          setTimeout(() => {
            console.log('Hello, World!')
            this.BubbleSort(newArray);
          }, 1);
          
          
        }
        else{
            return arrayToSort;
        }
      }

      HeapSort = (passedArrayToSort) =>{
        var length_of_heap = 500;
        for(let i=length_of_heap; i>0; i--){
          let maxHeap = this.BuildMaxHeap(passedArrayToSort, i);
          var heap = this.SwitchEndsOfHeap(maxHeap, i);
        }
        return heap
      }

      BuildMaxHeap(heap, length_of_heap){
        let swapped = true;
        let maxHeap;
        while(swapped){
          swapped = this.Heapify(this.state.arrayToSort, length_of_heap)
        }
        maxHeap = this.state.arrayToSort
        return maxHeap;
      }

      SwitchEndsOfHeap(heap, length_of_heap){
        let placeholder = heap[0];
        heap[0] = heap[length_of_heap];
        heap[length_of_heap] = placeholder;
        this.UpdateBarChart(heap);
        return heap;
      }
      
      Heapify(arrayToSort, lengthToSort){
            let heap = arrayToSort;
            let lengthToUse = (lengthToSort - 1)/2;
            let currentParent;
            let currentChildLeft;
            let currentChildRight;
            var swappedOnCurrentIter = false;

              for (let i=0; i < lengthToUse; i++){
                let x = 2*i+1;
                let y = 2*i+2;
                currentParent = heap[i];
                    currentChildLeft = heap[x];
                    currentChildRight = heap[y];
    
                    if(currentChildLeft > currentParent && currentChildLeft > currentChildRight){
                      heap[i] = currentChildLeft;
                      heap[x] = currentParent;
                      console.log("Swapped");
                      swappedOnCurrentIter = true;
                  }else if(currentChildRight > currentParent && currentChildRight >= currentChildLeft){
                      heap[i] = currentChildRight;
                      heap[y] = currentParent;
                      console.log("Swapped");
                      swappedOnCurrentIter = true;
                  }
                }
                this.UpdateBarChart(heap);
                return swappedOnCurrentIter;
            }
           
            


            
            // placeholderNode = heap[1];
            // heap[1] = heap[lengthToSort];
            // heap[lengthToSort] = placeholderNode;
            // if(swappedOnCurrentIter == true){
            //   let newLength = lengthToSort - 1;
            //   this.UpdateBarChart(heap);
            //   setTimeout(() => {
            //   this.Heapify(heap, newLength);
            //   }, 1);
            // }
            // else{
            //   console.log('FINISHED');
            //   return heap;
            // }
            
      
    


      UpdateBarChart(currentArray){
        let displayArray = this.CreateDisplayArrayFromArrayToSort(currentArray); 
        this.setState({
            arrayToSort : currentArray,
            chartData: displayArray
          })
    }    
    
      getChartData(){
        let arrayToSort = this.ResetToRandom();
        let displayArray = this.CreateDisplayArrayFromArrayToSort(arrayToSort);
        this.setState({ 
          arrayToSort: arrayToSort,
          chartData: displayArray
        })
      }
    
      CreateDisplayArrayFromArrayToSort(arrayToSort){
        let placeholderArray = [];
        let holdingArray = [500];
        holdingArray[0] = ['0-500','Entry Value'];
        for(let i=1; i<501;i++ ){
          placeholderArray[0] = i; 
          placeholderArray[1] = arrayToSort[i];
        
          holdingArray[i] = placeholderArray;
          placeholderArray = [];
        
        }
        return holdingArray;
      }
    
    render() {
        return (
          <div className={"my-pretty-chart-container"}>
            <button class="button-1" role="button" onClick= {() => {this.ResetOnclick()}}>Reset Data To Random</button>
            <Chart
              width={'1400px'}
              height={'500px'}
              chartType="Bar"
              loader={<div>Loading Chart</div>}
              data={
                this.state.chartData
              }
              options={{
                // Material design options
                chart: {
                  title: 'Randomized Data',
                  subtitle: 'Select a sort button to sort the data visually.',
                  //backgroundColor: 'red',
                },
                colors: ['#7509b0'],
              }}
              // For tests
              rootProps={{ 'data-testid': '2' }}
            />
            <button class="button-1" role="button" onClick= {() => {this.BubbleSort(this.state.arrayToSort)}}>Bubble Sort</button>
            <button class="button-1" role="button" onClick= {() => {this.HeapSort(this.state.arrayToSort)}}>Heap Sort</button>
            <button class="button-1" role="button" onClick= {() => {this.BubbleSort(this.state.arrayToSort)}}>Quick Sort</button>
            <button class="button-1" role="button" onClick= {() => {this.BubbleSort(this.state.arrayToSort)}}>Insert Sort</button>
            
          </div>
        );
      }
}export default GoogleChart;