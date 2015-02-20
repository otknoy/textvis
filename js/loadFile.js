var texts = [];

$('#files').change(function(e) {
    var files = e.target.files;
    var output = [];
    for (var i = 0; i < files.length; i++) {
	var file = files[i];

	loadFile(file).then(function(text) {
	    texts.push(text);

	    var $te = createTextElement(text);
	    console.log($te);
	    $('#texts').append($te);
	});
    }
});


function loadFile(file) {
    var d = Promise.defer();

    var reader = new FileReader();
    reader.readAsText(file);

    reader.onload = function(ev) {
	d.resolve(reader.result);
    };

    return d.promise;
}

function createTextElement(text) {
    var $div = $('<div>');

    var n = 32;
    console.log(text.length);
    if (text.length > n) {
	text = text.substr(0, n) + '...'; 
    }
    console.log(text);

    var $p = $('<p>').text(text);
    $div.append($p);

    return $div;
}
