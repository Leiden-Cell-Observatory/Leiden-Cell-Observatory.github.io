function initMicroscopeTable() {
  var table = document.getElementById("mic-data-table");
  if (!table || table.dataset.initialized) return;
  table.dataset.initialized = "true";

  var searchInput = document.getElementById("microscope-search");
  var filterContainer = document.getElementById("microscope-filters");
  var resultCount = document.getElementById("result-count");
  var clearBtn = document.getElementById("microscope-clear");
  if (!searchInput || !filterContainer || !resultCount) return;

  var rows = table.querySelectorAll("tbody tr");
  var totalCount = rows.length;
  var activeFilters = {};

  searchInput.addEventListener("input", function () {
    toggleClearButton();
    applyFilters();
  });

  if (clearBtn) {
    clearBtn.addEventListener("click", function () {
      searchInput.value = "";
      // Deactivate all chips
      filterContainer.querySelectorAll(".filter-chip.active").forEach(function (chip) {
        chip.classList.remove("active");
      });
      activeFilters = {};
      toggleClearButton();
      applyFilters();
    });
  }

  filterContainer.addEventListener("click", function (e) {
    var chip = e.target.closest(".filter-chip");
    if (!chip) return;
    chip.classList.toggle("active");
    updateActiveFilters();
    toggleClearButton();
    applyFilters();
  });

  function toggleClearButton() {
    if (!clearBtn) return;
    var hasSearch = searchInput.value.trim().length > 0;
    var hasFilters = filterContainer.querySelectorAll(".filter-chip.active").length > 0;
    clearBtn.style.display = (hasSearch || hasFilters) ? "inline-block" : "none";
  }

  function updateActiveFilters() {
    activeFilters = {};
    filterContainer.querySelectorAll(".filter-chip.active").forEach(function (chip) {
      var category = chip.getAttribute("data-category");
      var value = chip.getAttribute("data-value");
      if (!activeFilters[category]) {
        activeFilters[category] = new Set();
      }
      activeFilters[category].add(value.toLowerCase());
    });
  }

  function applyFilters() {
    var searchTerm = searchInput.value.toLowerCase().trim();
    var visibleCount = 0;

    rows.forEach(function (row) {
      var text = row.textContent.toLowerCase();
      var matchesSearch = !searchTerm || text.indexOf(searchTerm) !== -1;
      var matchesTags = matchesAllTagFilters(row);
      var visible = matchesSearch && matchesTags;
      row.style.display = visible ? "" : "none";
      if (visible) visibleCount++;
    });

    resultCount.textContent =
      "Showing " + visibleCount + " of " + totalCount + " microscopes";
  }

  function matchesAllTagFilters(row) {
    for (var category in activeFilters) {
      var values = activeFilters[category];
      if (values.size === 0) continue;

      var rowValue = (row.getAttribute("data-" + category) || "").toLowerCase();
      var matched = false;

      values.forEach(function (v) {
        if (rowValue.indexOf(v) !== -1) {
          matched = true;
        }
      });

      if (!matched) return false;
    }
    return true;
  }

  // Initialize
  toggleClearButton();
  applyFilters();

  // Init tablesort (only once via the guard above)
  if (typeof Tablesort !== "undefined") {
    new Tablesort(table);
  }
}

if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    initMicroscopeTable();
  });
} else {
  document.addEventListener("DOMContentLoaded", initMicroscopeTable);
}
