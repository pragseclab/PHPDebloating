<?php

/* table/search/search_and_replace.twig */
class __TwigTemplate_2707561c2d83084adff5de18e53c18305b3cf4123b4ea7a6169cbd857e74e1ff extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo _gettext("Find:");
        // line 2
        echo "<input type=\"text\" value=\"\" name=\"find\" required />
";
        // line 3
        echo _gettext("Replace with:");
        // line 4
        echo "<input type=\"text\" value=\"\" name=\"replaceWith\" />

";
        // line 6
        echo _gettext("Column:");
        // line 7
        echo "<select name=\"columnIndex\">
    ";
        // line 8
        $context['_parent'] = $context;
        $context['_seq'] = twig_ensure_traversable(range(0, (twig_length_filter($this->env, ($context["column_names"] ?? null)) - 1)));
        foreach ($context['_seq'] as $context["_key"] => $context["i"]) {
            // line 9
            echo "        ";
            $context["type"] = preg_replace("@\\(.*@s", "", $this->getAttribute(($context["column_types"] ?? null), $context["i"], array(), "array"));
            // line 10
            echo "        ";
            if (($this->getAttribute(($context["sql_types"] ?? null), "getTypeClass", array(0 => ($context["type"] ?? null)), "method") == "CHAR")) {
                // line 11
                echo "            ";
                $context["column"] = $this->getAttribute(($context["column_names"] ?? null), $context["i"], array(), "array");
                // line 12
                echo "            <option value=\"";
                echo twig_escape_filter($this->env, $context["i"], "html", null, true);
                echo "\">
                ";
                // line 13
                echo twig_escape_filter($this->env, ($context["column"] ?? null), "html", null, true);
                echo "
            </option>
        ";
            }
            // line 16
            echo "    ";
        }
        $_parent = $context['_parent'];
        unset($context['_seq'], $context['_iterated'], $context['_key'], $context['i'], $context['_parent'], $context['loop']);
        $context = array_intersect_key($context, $_parent) + $_parent;
        // line 17
        echo "</select>

";
        // line 19
        $this->loadTemplate("checkbox.twig", "table/search/search_and_replace.twig", 19)->display(array("html_field_id" => "useRegex", "html_field_name" => "useRegex", "label" => _gettext("Use regular expression"), "checked" => false, "onclick" => false));
    }

    public function getTemplateName()
    {
        return "table/search/search_and_replace.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  69 => 19,  65 => 17,  59 => 16,  53 => 13,  48 => 12,  45 => 11,  42 => 10,  39 => 9,  35 => 8,  32 => 7,  30 => 6,  26 => 4,  24 => 3,  21 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "table/search/search_and_replace.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/table/search/search_and_replace.twig");
    }
}
