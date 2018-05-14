/*
 * A Design by GraphBerry
 * Author: GraphBerry
 * Author URL: http://graphberry.com
 * License: http://graphberry.com/pages/license
 */
$(function(){
	'use strict';

	var options ={
		wrapper: ".wrapper",
		minHeight: 500
	};

	function setHeight(){
		var documentHeight = $(window).height();

		if(documentHeight > options.minHeight){
			$(options.wrapper).height(documentHeight);
		}
	}

	setHeight();

	$(window).resize(function(){
		setHeight();
	})

	$('.countdown').downCount({
                    date: '05/17/2015 9:00:00',
                    offset: +10
                }, function() {

                });


});