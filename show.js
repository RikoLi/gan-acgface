const model = new KerasJS.Model({
    filepath: '../gan_models/12.12/generator.bin',
    gpu: true
});

let noise = [];
for(let i = 0; i < 100; i++){
    noise.splice(i, 0, Math.random()-1);
}

model
  .ready()
  .then(() => {
    // input data object keyed by names of the input layers
    // or `input` for Sequential models
    // values are the flattened Float32Array data
    // (input tensor shapes are specified in the model config)
    const inputData = {
        input_1: new Float32Array(noise)
    }

    // make predictions
    return model.predict(inputData)
  })
  .then(outputData => {
    // outputData is an object keyed by names of the output layers
    // or `output` for Sequential models
    // e.g.,
    // outputData['fc1000']
  })
  .catch(err => {
    // handle error
  })

let show_input = document.getElementById('input');
show_input.innerHTML = noise;
