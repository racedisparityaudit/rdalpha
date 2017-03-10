Rails.application.routes.draw do
  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  #TODO: KASM make roots
  root 'homepage#index'

  post 'navigation_form' => 'homepage#navigation_form'
  get 'attainment8/metadata' => 'taxonomy_level#metadata'
  get 'factoids/:race' => 'taxonomy_level#factoids'
  post 'topics/:filter' => 'taxonomy_level#topics'
  get 'topics/:filter' => 'taxonomy_level#topics'
  get 'topics/:filter/:race' => 'taxonomy_level#topics'

  get 'question/:question' => 'taxonomy_level#question'
  get ':taxonomy_name' => 'taxonomy_level#show'
  get ':parent_name/:taxonomy_name' => 'taxonomy_level#show'

end
