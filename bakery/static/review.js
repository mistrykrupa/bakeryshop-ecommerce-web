/*
console.log("working fine");

$("#reviewrating").submit(function(e){
    e.preventDefault();

    $.ajax({
        data :$(this).serialize(),
        method:$(this).attr("method"),
        url :$(this).attr("action"),
        dataType :"json",
        success : function(res){
            console.log("Comment Saved to DB..");
            if(res.bool == true){
                $("#review-res").html("Review added successfully.")
                $(".hidden").hide()


                 // Update average rating if available
                 if(res.context.average_rating !== null){
                    $("#average-rating").text("Average Rating: " + res.context.average_rating.toFixed(1));
                 }
            }
        }

    })
})
*/
// some scripts

// jquery ready start
/*$(document).ready(function() {
	// jQuery code


     ///////////////////////////////////////

    THESE FOLLOWING SCRIPTS ONLY FOR BASIC USAGE,
    For sliders, interactions and other

    ///////////////////////////////////////


	//////////////////////// Prevent closing from click inside dropdown
    $(document).on('click', '.dropdown-menu', function (e) {
      e.stopPropagation();
    });


    $('.js-check :radio').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $('input[name='+ check_attr_name +']').closest('.js-check').removeClass('active');
            $(this).closest('.js-check').addClass('active');
           // item.find('.radio').find('span').text('Add');

        } else {
            item.removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });


    $('.js-check :checkbox').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $(this).closest('.js-check').addClass('active');
           // item.find('.radio').find('span').text('Add');
        } else {
            $(this).closest('.js-check').removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });



	//////////////////////// Bootstrap tooltip
	if($('[data-toggle="tooltip"]').length>0) {  // check if element exists
		$('[data-toggle="tooltip"]').tooltip()
	} // end if





});
// jquery end

setTimeout(function(){
  $('#message').fadeOut('slow')
}, 4000)*/


$(document).ready(function() {
    function fetchAdditionalReviews() {
        // Send an AJAX request to fetch additional reviews
        $.ajax({
            type: "GET",
            url: "{% url 'fetch_additional_reviews' %}",  // Update with your URL endpoint
            dataType: "json",
            success: function (response) {
                // Append additional reviews to the existing reviews section
                response.reviews.forEach(function (review) {
                    var newReview = "<li><div class='review'><p><strong>User:</strong> " + review.user + "</p><p><strong>Rating:</strong> " + review.rating + "</p><p><strong>Review:</strong> " + review.review + "</p></div></li>";
                    $(".additional-reviews ").append(newReview);
                });
            },
            error: function (xhr, status, error) {
                console.error("Error fetching additional reviews:", error);
            }
        });
    }
    // Submit review form via AJAX
    $("#reviewrating").submit(function(e) {
        e.preventDefault();
        
        $.ajax({
            type: "POST",
            

            url: $(this).attr("action"),
            data: $(this).serialize(),
            dataType: "json",
            success: function(response) {
                if (response.success) {
                    // Display success message
                    $("#review-res").text("Review added successfully.");
                    
                    // Clear review text
                    $("#review-text").val("");
                    
                    // Update average rating if available
                    if (response.context.average_rating !== null) {
                        $("#average-rating").text("Average Rating: " + response.context.average_rating.toFixed(1));
                    }
                    
                    // Optionally, you can append the new review to the existing reviews section
                    var newReview = "<div class='review'><p><strong>User:</strong> " + response.context.user + "</p><p><strong>Rating:</strong> " + response.context.rating + "</p><p><strong>Review:</strong> " + response.context.review + "</p></div>";
                    $(".reviews ul").append("<li>" +newReview + "</li>");
                } else {
                    // Display error message if review submission fails
                    $("#review-res").text("Error: " + response.error);
                }
            },
            error: function(xhr, status, error) {
                // Display error message if AJAX request fails
                $("#review-res").text("Error: " + xhr.responseText);
            }
        });
    });



    // Toggle visibility of additional reviews
    $("#view-more-reviews").click(function() {
        fetchAdditionalReviews();  // Call the function to fetch additional reviews
        $(this).hide();// Hide the "View More Reviews" button
        
    });


    /* $('.plus-wishlist').click(function(){
        var id=$(this).attr("pid").toString();
        $.ajax({
            type:"GET",
            url:"/pluswishlist",
            data:{
                prod_id:id
            },
            success:function(data){
                //alert(data.message)
                window.location.href = `http://localhost:8000/product-detail/${id}`
            }
        })
    })
    
    
    $('.minus-wishlist').click(function(){
        var id=$(this).attr("pid").toString();
        $.ajax({
            type:"GET",
            url:"/minuswishlist",
            data:{
                prod_id:id
            },
            success:function(data){
                window.location.href = `http://localhost:8000/product-detail/${id}`
            }
        })
    })*/


    /*$('.addToWishlist').click(function (e){
        e.preventDefault();
        var item_id=$(this).closet('.card').find('.id').val();
        var token = $('input[name=csrfmiddlewaretoke]').val();

        $.ajax({
            method:"POST",
            url:"/add-to-wishlist",
            data:{
                item_id:item_id,
                csrfmiddlewaretoken:token
            },
            success:function(response){
                alertify.success(request.status)
               
            }
        })
    })*/

    $('.add-to-wishlist').click(function(){
        var id = $(this).data("id");
        $.ajax({
            type: "POST",  // Use POST method for adding items to the wishlist
            url: "/add_to_wishlist/" + id + "/",
            /*data: {
                item_id: id
            },*/
            success: function(response) {
                if (response.success) {
                    // Item added to wishlist successfully
                    alert("Item added to wishlist!");
                } else {
                    // Error occurred while adding item to wishlist
                    alert("Failed to add item to wishlist. Please try again later.");
                }
            },
            error: function(xhr, status, error) {
                // Error handling for AJAX request
                console.error("Error:", error);
            }
        });
    });
    
    // JavaScript for removing an item from the wishlist
    $('.remove-from-wishlist').click(function(){
        var id = $(this).data("id");
        $.ajax({
            type: "POST",  // Use POST method for removing items from the wishlist
            url: "/remove_from_wishlist/" + id + "/",
            /*data: {
                item_id: id
            },*/
            success: function(response) {
                if (response.success) {
                    // Item removed from wishlist successfully
                    alert("Item removed from wishlist!");
                } else {
                    // Error occurred while removing item from wishlist
                    alert("Failed to remove item from wishlist. Please try again later.");
                }
            },
            error: function(xhr, status, error) {
                // Error handling for AJAX request
                console.error("Error:", error);
            }
        });
    });
 });

 function removeItem(button) {
    const row = button.parentElement.parentElement;
    row.remove();
    updateTotal();
  }

    




