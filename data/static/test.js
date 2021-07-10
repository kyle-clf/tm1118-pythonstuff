$.ajax({
    type: 'POST',
    url: '/query/result',
    data: {
'start' : document.getElementById('inputTimeStart').value,
'end' : document.getElementById('inputTimeEnd').value,
'location' : document.getElementById('inputLocation').value,
},
    complete: function () {
     
    },
    success: function (data) {
dataset = JSON.parse(data); 
dataset['events'] = JSON.parse(dataset['events']); 
dataset['events'].forEach((e, idx) => dataset['events'][idx] = e['fields'])
console.log(dataset);
    }
});