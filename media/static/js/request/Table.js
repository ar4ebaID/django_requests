$(document).ready(function() {
    $('#table').DataTable({
        stateSave: true,
        searching: false,
        info: false,
        "aaSorting": [[ 0,"desc" ]],
        "aLengthMenu": [[ 5, 10, 15, 20, 50, 100 ,-1],[5,10,15,20,50,100,"все"]],
            language: {"lengthMenu": "Показать _MENU_ записей",
                "emptyTable": "В таблице отсутствуют данные",
                "paginate": {"first": "Первая",
                "previous": "Предыдущая",
                "next": "Следующая",
                "last": "Последняя"}},
    });
});