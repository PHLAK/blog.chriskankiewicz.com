$(document).ready(function() {

    // Enable Tooltips
    $('[rel="tooltip"]').tooltip();

    // Site search on submit action
    $('.site-search').submit(function(event) {

        // Prevent default action
        event.preventDefault();

        // Get the search text
        var searchText = $('.site-search .search-text').val().trim();

        if (searchText !== '') {

            // URL encode the search text
            var encodedText = encodeURIComponent(searchText).replace(/%20/g, '+');

            // Create the full search URL
            var searchURL = 'https://encrypted.google.com/#q=' + siteURL + '+' + encodedText;

            // Redirect page
            window.location.replace(searchURL);

        }

    })

});
