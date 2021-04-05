$('#btn').click(function(){ 
    let csrf=document.querySelector('input[name="csrfmiddlewaretoken"]').value
    let btn=document.getElementById('inp1').value
    var form={
        'value':btn,
        'csrfmiddlewaretoken':csrf

    }
    $.ajax({
        type:'POST',
        url:'http://127.0.0.1:8000/new',
        data:form,
        encoded:true

    })
    .done((data)=>{
        document.getElementById('sec1').value=`http://127.0.0.1:8000/${data}`
        alert("Shorted Sucsessfully")
    })
})