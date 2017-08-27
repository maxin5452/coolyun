var tab1 = document.getElementById('tab1'),
                tab2 = document.getElementById('tab2'),
                tab3 = document.getElementById('tab3'),
				tag4 = document.getElementById('tab4'),
				tag5 = document.getElementById('tab5'),
                c1 = document.getElementById('c1'),
                c2 = document.getElementById('c2'),
                c3 = document.getElementById('c3'),
				c4 = document.getElementById('c4'),
				c5 = document.getElementById('c5');

            function changeTab1() {
                tab1.className = 'selected';
                tab2.className = '';
                tab3.className = '';
				tag4.className = '';
				tag5.className = '';
                c1.className = 'show';
                c2.className = '';
                c3.className = '';
				c4.className = '';
				c5.className = '';
            }

            function changeTab2() {
                tab1.className = '';
                tab2.className = 'selected';
                tab3.className = '';
				tag4.className = '';
				tag5.className = '';
                c1.className = '';
                c2.className = 'show';
                c3.className = '';
				c4.className = '';
				c5.className = '';
            }

            function changeTab3() {
                tab1.className = '';
                tab2.className = '';
                tab3.className = 'selected';
				tab4.className = '';
				tag5.className = '';
                c1.className = ''
                c2.className = '';
                c3.className = 'show';
				c4.className = '';
				c5.className = '';
            }
			
			 function changeTab4() {
                tab1.className = '';
                tab2.className = '';
                tab3.className = '';
				tab4.className = 'selected';
				tag5.className = '';
                c1.className = ''
                c2.className = '';
                c3.className = '';
				c4.className = 'show';
				c5.className = '';
            }
			
			 function changeTab5() {
                tab1.className = '';
                tab2.className = '';
                tab3.className = '';
				tab4.className = '';
				tag5.className = 'selected';
                c1.className = ''
                c2.className = '';
                c3.className = '';
				c4.className = '';
				c5.className = 'show';
            }
			