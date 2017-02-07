class AddFieldsToTaxonomyLevel < ActiveRecord::Migration[5.0]
  def change
    add_column :taxonomy_levels, :description, :string
    add_column :taxonomy_levels, :uri, :string
    add_column :taxonomy_levels, :source, :string


  end
end
