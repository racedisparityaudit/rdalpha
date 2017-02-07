Rails.application.routes.draw do
  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  root 'homepage#index'

  get ':taxonomy_name' => 'taxonomy_level#show'
  get ':parent_name/:taxonomy_name' => 'taxonomy_level#show'
  get ':parent_name/:taxonomy_name' => 'taxonomy_level#show'

  get ':parent_name/:taxonomy_name/:question' => 'taxonomy_level#question'

end
