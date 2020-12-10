import React from "react";

import { EditorState,Editor as DraftEditor } from "draft-js";



export default class Editor extends React.Component{
    constructor(props){
        super(props)
        this.state={
            editorState: EditorState.createEmpty()
        }
        // this.updateEditorState=this.updateEditorState.bind(this)
    }

    updateEditorState(editorState){
        this.setState({editorState})
    }
    render(){
        return(
            <div className="editor-container">
                    <DraftEditor
                        placeholder="Type something..."
                        editorState={this.state.editorState}
                        onChange={this.updateEditorState.bind(this)}
                    />
            </div>
        )
    }
}