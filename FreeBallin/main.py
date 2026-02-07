def count_nested_levels(nested_documents, target_document_id, level=1):
    
    for document_id, children in nested_documents.items():
        
        if document_id == target_document_id:
            return level
        
        result = count_nested_levels(children, target_document_id, level + 1)

        if result != -1:
            return result
        
    return -1

