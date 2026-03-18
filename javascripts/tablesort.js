document$.subscribe(function () {
  var tables = document.querySelectorAll("article table:not([class]):not(#mic-data-table)");
  tables.forEach(function (table) {
    new Tablesort(table);
  });
});
