/*
    navbar loaded by the DOM with javascript
    better method since adding / editing navbar items is way easier
*/
var navbar = document.getElementById("navbarhome");

//create navbar parent
var navbarToggler = document.createElement("button");
navbarToggler.className="navbar-toggler";
navbarToggler.type="button";
navbarToggler.setAttribute("data-toggle","collapse");
navbarToggler.setAttribute("data-target","#collapseNavv");
navbarToggler.setAttribute("aria-expanded","false");
navbarToggler.setAttribute("aria-label","Toggle navigation");
var navbarTogglerSpan = document.createElement("span");
navbarTogglerSpan.className="navbar-toggler-icon"
navbarToggler.appendChild(navbarTogglerSpan);
navbar.appendChild(navbarToggler);

//containers - navbar + collapsed (on mobile)
var containerFluid = document.createElement("div");
containerFluid.className="container-fluid";
var collapseNav = document.createElement("div");
collapseNav.className="collapse navbar-collapse";
collapseNav.id="collapseNavv";
containerFluid.appendChild(collapseNav);
navbar.appendChild(containerFluid);

//icon/home link
var navbarBrand = document.createElement("a");
navbarBrand.className="navbar-brand";
navbarBrand.href="./index.html";
var navbarBrandImg = document.createElement("img");
navbarBrandImg.src="./hippoHackLogo.png";
navbarBrandImg.alt="Logo";
navbarBrandImg.style.width="40px";
navbarBrand.appendChild(navbarBrandImg);
collapseNav.appendChild(navbarBrand);

//navbar list
var navbarList = document.createElement("ul");
navbarList.className="navbar-nav ml-auto";

/**
 * String [title]: title of the button
 * String [link]: redir link for the button
 * Node/Element [location]: the element (or node whatever) AS TYPE ELEMENT that the navbar button is going to be appended to
 */
var createNavbarButton = function (title,link,location) {

    //create the li in the list
    var item = document.createElement("li");
    item.className="nav-item";

    //create the link
    var itemLink = document.createElement("a");
    itemLink.className="nav-link dropdown";
    itemLink.innerHTML=title;
    itemLink.href=link;
    
    item.appendChild(itemLink);
    location.appendChild(item);

}

/**
 * String [title]: title of the list
 * Set [items] of a Set of String attributes: items with attributes of the list
 *   String[][] items
 * Map of: String item title [items]  to  Set of items filled with Set(s) of String attributes: items with attributes of the list under a label
 *   HashMap<String,String[]> items
 *      <note: since params are non-typed, pass either a set or a map for items (this is essentially overloading)>
 * Node/Element [location]: the element (or node whatever) AS TYPE ELEMENT that the navbar button is going to be appended to
 */
var createNavbarList = function (title,items,location) {
    
    //create the li in the list
    var item = document.createElement("li");
    item.className="nav-item dropdown";

    var listTitle = document.createElement("a");
    listTitle.href="#";
    listTitle.className="nav-link dropdown-toggle";
    listTitle.id="navbardrop"; //redundant...
    listTitle.setAttribute("data-toggle","dropdown");
    listTitle.innerHTML=title;

    var listContainer = document.createElement("div");
    listContainer.className="dropdown-menu";

    if (Array.isArray(items)){
        for (var i=0;i<items.length;i++){
            var listItem = document.createElement("a");
            listItem.className="dropdown-item special-hover";
            listItem.innerHTML=items[i][0];
            listItem.href=items[i][1];
            listContainer.appendChild(listItem);
        }
    }else{
        var keys = Object.keys(items);
        for (var i=0;i<keys.length;i++){
            var subtitle = document.createElement("h6");
            subtitle.className="dropdown-header pl-3";
            subtitle.innerHTML=keys[i];
            listContainer.appendChild(subtitle);
            for (var j=0;j<(items[keys[i]]).length;j++){
                var listItem = document.createElement("a");
                listItem.className="dropdown-item special-hover";
                listItem.innerHTML=(items[keys[i]][j])[0];
                listItem.href=(items[keys[i]][j])[1];
                listContainer.appendChild(listItem);
            }
        }
    }

    item.appendChild(listTitle);
    item.appendChild(listContainer);
    location.appendChild(item);

}

//do the list item creation!!
//parent: navbarList
//createNavbarList, createNavbarButton
//item's attributes list: [title, link]

createNavbarButton( )

collapseNav.appendChild(navbarList);