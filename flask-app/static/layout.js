'use strict';

const e = React.createElement;


class Layout extends React.Component {
    constructor(props){
        super(props);
    }

}

const domContainer = document.querySelector('#pageLayout');
ReactDOM.render(e(Layout), domContainer);